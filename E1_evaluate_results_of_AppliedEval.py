#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import re
import subprocess
import tempfile
import os
import traceback
import argparse
from typing import Any, List, Tuple


def extract_code(response: str) -> str:
    """
    Return only the Python code from the LLM response.
    First tries for ```python ... ```, then for ``` ... ```, otherwise returns the whole response.
    """
    if not isinstance(response, str):
        return ""
    # ```python ... ```
    m = re.findall(r"```python\s*(.*?)```", response, flags=re.DOTALL | re.IGNORECASE)
    if m:
        return m[0].strip()
    # ``` ... ```
    m = re.findall(r"```\s*(.*?)```", response, flags=re.DOTALL)
    if m:
        return m[0].strip()
    return response.strip()


def py_repr(obj: Any) -> str:
    """
    Convert Python objects (originating from JSON) to a source literal for embedding in code.
    Handles conversion of None (from JSON null) specially.
    """
    if obj is None:
        return "None"
    return repr(obj)


def results_equivalent(result: Any, expected: Any) -> bool:
    """
    Flexible comparison that focuses on logical equivalence rather than exact formatting.
    Handles common cases where results are logically the same but formatted differently.
    """
    # Direct equality first
    if result == expected:
        return True
    
    # Handle None/null equivalence
    if result is None and expected is None:
        return True
    
    # For lists/tuples - convert both to lists and compare
    if isinstance(result, (list, tuple)) and isinstance(expected, (list, tuple)):
        return list(result) == list(expected)
    
    # For dictionaries - compare after sorting keys (for consistent ordering)
    if isinstance(result, dict) and isinstance(expected, dict):
        if set(result.keys()) != set(expected.keys()):
            return False
        for key in result.keys():
            if not results_equivalent(result[key], expected[key]):
                return False
        return True
    
    # For sets - compare as sets
    if isinstance(result, set) and isinstance(expected, set):
        return result == expected
    
    # For strings - strip whitespace and compare
    if isinstance(result, str) and isinstance(expected, str):
        return result.strip() == expected.strip()
    
    # For numbers - handle float precision issues
    if isinstance(result, (int, float)) and isinstance(expected, (int, float)):
        return abs(result - expected) < 1e-9
    
    return False


def is_class_based_task(test_cases: List[Tuple[Any, Any]]) -> bool:
    """
    Check whether the task is class-based (like MinStack, LRUCache)
    based on the format of the test cases.
    """
    if not test_cases:
        return False
    
    first_input, _ = test_cases[0]
    # Class-based tasks have input format: [["ClassName", "method1", "method2", ...], [[], [arg1], [arg2], ...]]
    if (isinstance(first_input, list) and len(first_input) == 2 and
        isinstance(first_input[0], list) and isinstance(first_input[1], list) and
        len(first_input[0]) > 0 and isinstance(first_input[0][0], str)):
        return True
    return False


def build_function_test_harness_flexible(entry_point: str, cases: List[Tuple[Any, Any]]) -> str:
    """
    Create a test harness for function-based tasks that finds any function,
    regardless of its name.
    """
    py_cases = []
    for args, expected in cases:
        args_src = py_repr(args)
        expected_src = py_repr(expected)
        py_cases.append(f"({args_src}, {expected_src})")
    cases_block = ",\n    ".join(py_cases)

    harness = f"""
# ----- AUTO-GENERATED FLEXIBLE FUNCTION TEST HARNESS -----
import ast
import types

def results_equivalent(result, expected):
    \"\"\"Flexible comparison for logical equivalence\"\"\"
    if result == expected:
        return True
    if result is None and expected is None:
        return True
    if isinstance(result, (list, tuple)) and isinstance(expected, (list, tuple)):
        return list(result) == list(expected)
    if isinstance(result, dict) and isinstance(expected, dict):
        if set(result.keys()) != set(expected.keys()):
            return False
        for key in result.keys():
            if not results_equivalent(result[key], expected[key]):
                return False
        return True
    if isinstance(result, str) and isinstance(expected, str):
        return result.strip() == expected.strip()
    if isinstance(result, (int, float)) and isinstance(expected, (int, float)):
        return abs(result - expected) < 1e-9
    return False

def find_user_function():
    \"\"\"
    Find the first user-defined function in the global namespace.
    Returns the function or None if not found.
    \"\"\"
    import inspect
    
    # Get all objects from the global namespace
    current_globals = globals()
    
    user_functions = []
    for name, obj in current_globals.items():
        # Check if it is a function and not built-in
        if (isinstance(obj, types.FunctionType) and 
            not name.startswith('__') and 
            name not in ['results_equivalent', 'find_user_function', '__run_tests__']):
            user_functions.append(obj)
    
    if len(user_functions) == 1:
        return user_functions[0]
    elif len(user_functions) > 1:
        # If there are multiple, try to find one that matches the expected name
        for func in user_functions:
            if func.__name__ == '{entry_point}':
                return func
        # Otherwise return the first one
        return user_functions[0]
    else:
        return None

def __run_tests__():
    # First try to get the function with the correct name
    try:
        fn = {entry_point}
    except NameError:
        # If it does not exist, search for any user function
        fn = find_user_function()
        if fn is None:
            raise AssertionError("No user-defined function found in the code.")

    CASES = [
    {cases_block}
    ]

    passed = 0
    total = 0
    for i, (args, expected) in enumerate(CASES):
        total += 1
        try:
            # For function-based tasks, args is usually a list of arguments
            if isinstance(args, list):
                result = fn(*args)
            else:
                result = fn(args)
            
            if not results_equivalent(result, expected):
                raise AssertionError(f"Case {{i}} failed: result={{result!r}} expected={{expected!r}}")
            passed += 1
        except Exception as e:
            raise AssertionError(f"Case {{i}} failed with exception: {{str(e)}}")

    print(f"__RESULT__:{{passed}}/{{total}}")

if __name__ == "__main__":
    __run_tests__()
"""
    return harness


def build_class_test_harness(entry_point: str, cases: List[Tuple[Any, Any]]) -> str:
    """
    Create a test harness for class-based tasks (such as MinStack, LRUCache).
    """
    if not cases:
        return ""
    
    # Use the first test case to inspect the structure
    first_input, first_expected = cases[0]
    methods = first_input[0]  # ["MinStack", "push", "push", ...]
    args_list = first_input[1]  # [[], [-2], [0], ...]
    expected_list = first_expected  # [null, null, null, ...]
    
    py_cases = []
    for args, expected in cases:
        methods_src = py_repr(args[0])
        args_list_src = py_repr(args[1])
        expected_src = py_repr(expected)
        py_cases.append(f"({methods_src}, {args_list_src}, {expected_src})")
    
    cases_block = ",\n    ".join(py_cases)

    harness = f"""
# ----- AUTO-GENERATED CLASS TEST HARNESS -----
def results_equivalent(result, expected):
    \"\"\"Flexible comparison for logical equivalence\"\"\"
    if result == expected:
        return True
    if result is None and expected is None:
        return True
    if isinstance(result, (list, tuple)) and isinstance(expected, (list, tuple)):
        return list(result) == list(expected)
    if isinstance(result, dict) and isinstance(expected, dict):
        if set(result.keys()) != set(expected.keys()):
            return False
        for key in result.keys():
            if not results_equivalent(result[key], expected[key]):
                return False
        return True
    if isinstance(result, str) and isinstance(expected, str):
        return result.strip() == expected.strip()
    if isinstance(result, (int, float)) and isinstance(expected, (int, float)):
        return abs(result - expected) < 1e-9
    return False

def __run_tests__():
    try:
        cls = {entry_point}
    except NameError:
        raise AssertionError("Entry point '{entry_point}' is not defined by the LLM code.")

    CASES = [
    {cases_block}
    ]

    passed = 0
    total = 0
    for case_idx, (methods, args_list, expected_list) in enumerate(CASES):
        total += 1
        
        if len(methods) != len(args_list) or len(methods) != len(expected_list):
            raise AssertionError(f"Case {{case_idx}}: Length mismatch in test data")
        
        obj = None
        for i, (method_name, method_args, expected) in enumerate(zip(methods, args_list, expected_list)):
            if i == 0:  # Constructor
                if method_args:
                    obj = cls(*method_args)
                else:
                    obj = cls()
                result = None  # Constructor calls return None
            else:
                # Method call
                method = getattr(obj, method_name)
                if method_args:
                    result = method(*method_args)
                else:
                    result = method()
            
            if not results_equivalent(result, expected):
                raise AssertionError(f"Case {{case_idx}}, step {{i}} ({{method_name}}): result={{result!r}} expected={{expected!r}}")
        
        passed += 1

    print(f"__RESULT__:{{passed}}/{{total}}")

if __name__ == "__main__":
    __run_tests__()
"""
    return harness


def normalize_tests(raw_tests: Any) -> List[Tuple[Any, Any]]:
    """
    Take raw_item['test'] and convert it to a list of (input, output) tuples.
    """
    cases = []
    if not isinstance(raw_tests, list):
        return cases
    for t in raw_tests:
        if not isinstance(t, dict):
            continue
        if "input" not in t or "output" not in t:
            continue
        cases.append((t["input"], t["output"]))
    return cases


def run_file_and_capture(py_code: str, timeout: float) -> Tuple[bool, str]:
    """
    Write a temporary .py file (LLM code + harness) and run it with python3.
    """
    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tmp:
            tmp.write(py_code)
            tmp.flush()
            tmp_path = tmp.name

        proc = subprocess.run(
            ["python3", tmp_path],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        if proc.returncode == 0 and "__RESULT__" in out:
            return True, out
        else:
            return False, out
    except subprocess.TimeoutExpired:
        return False, "TimeoutExpired"
    except Exception as e:
        return False, traceback.format_exc()
    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.unlink(tmp_path)


def main():
    parser = argparse.ArgumentParser(description="Evaluate LLM results against structured tests.")
    parser.add_argument("--results", default="results2.jsonl", help="Path to results JSONL (LLM outputs).")
    parser.add_argument("--out", default="evaluation_report.jsonl", help="Path to write evaluation report JSONL.")
    parser.add_argument("--timeout", type=float, default=8.0, help="Per-test Python execution timeout (seconds).")
    parser.add_argument("--verbose", action="store_true", help="Print more info (skipped entries etc.).")
    args = parser.parse_args()

    results_file = args.results
    report_file = args.out

    total, passed = 0, 0
    evaluated = 0

    with open(results_file, "r", encoding="utf-8") as f_in, open(report_file, "w", encoding="utf-8") as f_out:
        for line in f_in:
            item = json.loads(line)
            dataset_index = item.get("dataset_index", -1)
            raw = item.get("raw_item", {})

            # 1) code from LLM
            llm_code = extract_code(item.get("response", ""))

            # 2) entry point
            entry_point = raw.get("entry_point")
            if not isinstance(entry_point, str) or not entry_point.strip():
                if args.verbose:
                    print(f"⚠️  Skipping index {dataset_index}: missing entry_point")
                continue

            # 3) tests -> cases
            cases = normalize_tests(raw.get("test"))
            if not cases:
                if args.verbose:
                    print(f"⚠️  Skipping index {dataset_index}: no structured test cases")
                continue

            # if there is no code at all, skip
            if not llm_code.strip():
                if args.verbose:
                    print(f"⚠️  Skipping index {dataset_index}: empty LLM code")
                continue

            # 4) Decide if the task is function or class-based
            if is_class_based_task(cases):
                harness = build_class_test_harness(entry_point.strip(), cases)
            else:
                # Use the flexible function harness instead
                harness = build_function_test_harness_flexible(entry_point.strip(), cases)

            full_code = llm_code + "\n\n" + harness

            success, output = run_file_and_capture(full_code, timeout=args.timeout)
            evaluated += 1
            total += 1
            if success:
                passed += 1

            # write a detailed report per item
            f_out.write(json.dumps({
                "dataset_index": dataset_index,
                "task_id": raw.get("task_id", "unknown"),
                "entry_point": entry_point,
                "passed": success,
                "runner_output": output,
                "is_class_based": is_class_based_task(cases)
            }, ensure_ascii=False) + "\n")

            # short console output
            if args.verbose:
                status = "✅" if success else "❌"
                task_type = "class" if is_class_based_task(cases) else "func"
                print(f"{status} index {dataset_index} ({entry_point}) [{task_type}]")

    print("✅ Evaluation completed!")
    if total > 0:
        print(f"📊 Accuracy: {passed}/{total} = {passed/total:.2%}")
    else:
        print("⚠️ No testable items were found (missing entry_point/tests or empty code).")
    print(f"📂 Detailed report saved to {report_file}")


if __name__ == "__main__":
    main()