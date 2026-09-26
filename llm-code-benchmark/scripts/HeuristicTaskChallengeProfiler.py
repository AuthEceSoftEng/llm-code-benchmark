#!/usr/bin/env python3
import json, re, argparse, csv, ast
from pathlib import Path
from typing import Any, Dict

TEST_PATTERNS = {
    "has_negative": re.compile(r"(?<![\w])-\d"),
    "has_zero": re.compile(r"(?<![\w])0(?!\.)"),
    "has_large_int": re.compile(r"\b\d{5,}\b"),
    "has_float": re.compile(r"\d+\.\d+|\d+e-?\d+|\d+\.0e-?\d+", re.IGNORECASE),
    "has_empty_list": re.compile(r"\[\s*\]"),
    "has_empty_str": re.compile(r"(?<!\\)''|(?<!\\)\"\""),
    "has_none": re.compile(r"(?<!\w)None(?!\w)"),
    "has_unicode": re.compile(r"[^\x00-\x7F]"),
    "has_exception": re.compile(r"try:|except\s+[A-Za-z_]\w*:", re.IGNORECASE),
    "has_whitespace_edge": re.compile(r"['\"][^'\"]*\\n|\\t|\\r|\\s['\"]"),
}

CONSTRAINT_WORDS = [
    "must", "should", "always", "never",
    "edge case", "corner case", "robust", "handle", "invalid", "raise",
    "assume", "guarantee", "strictly", "exactly"
]

def to_text(x: Any) -> str:
    if isinstance(x, list):
        return "\n\n".join(str(i) for i in x)
    return str(x or "")

class FeatureVisitor(ast.NodeVisitor):
    def __init__(self, entry_point: str):
        self.entry_point = entry_point
        self.branching = 0
        self.loops = 0
        self.tries = 0
        self.raises = 0
        self.calls = 0
        self.comprehensions = 0
        self.recursive_calls = 0
        self.max_depth = 0
        self._depth = 0

    def generic_visit(self, node):
        is_block = isinstance(node, (ast.If, ast.For, ast.While, ast.Try, ast.With, ast.FunctionDef, ast.AsyncFunctionDef))
        if is_block:
            self._depth += 1
            self.max_depth = max(self.max_depth, self._depth)
        if isinstance(node, ast.If):
            self.branching += 1
        if isinstance(node, (ast.For, ast.While)):
            self.loops += 1
        if isinstance(node, ast.Try):
            self.tries += 1
        if isinstance(node, ast.Raise):
            self.raises += 1
        if isinstance(node, ast.Call):
            self.calls += 1
            if isinstance(node.func, ast.Name) and node.func.id == self.entry_point:
                self.recursive_calls += 1
        if isinstance(node, (ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)):
            self.comprehensions += 1

        super().generic_visit(node)
        if is_block:
            self._depth -= 1

def ast_features(code: str, entry_point: str):
    try:
        tree = ast.parse(code)
    except Exception:
        return {
            "branching_count": 0, "loop_count": 0, "try_count": 0, "raise_count": 0,
            "call_count": 0, "comprehension_count": 0, "recursion_calls": 0, "max_nesting_depth": 0
        }
    v = FeatureVisitor(entry_point or "")
    v.visit(tree)
    return {
        "branching_count": v.branching,
        "loop_count": v.loops,
        "try_count": v.tries,
        "raise_count": v.raises,
        "call_count": v.calls,
        "comprehension_count": v.comprehensions,
        "recursion_calls": v.recursive_calls,
        "max_nesting_depth": v.max_depth,
    }

def prompt_features(prompt: str):
    p = prompt or ""
    lower = p.lower()
    constraints = 0
    for w in CONSTRAINT_WORDS:
        constraints += lower.count(w)
    return {
        "prompt_length": len(p),
        "constraint_markers": constraints
    }

def test_features(test_text: str):
    s = test_text or ""
    out = {"num_asserts": len(re.findall(r"(?<![A-Za-z_])assert(?![A-Za-z_])", s))}
    for k, pat in TEST_PATTERNS.items():
        out[k] = bool(pat.search(s))
    return out

def score_row(row):
    w = {
        "branching_count": 2.0,
        "loop_count": 1.8,
        "try_count": 1.5,
        "raise_count": 1.2,
        "call_count": 0.5,
        "comprehension_count": 0.7,
        "recursion_calls": 2.5,
        "max_nesting_depth": 2.0,
        "prompt_length": 0.003,
        "constraint_markers": 1.0,
        "num_asserts": 0.2,
        "has_negative": 0.6,
        "has_zero": 0.4,
        "has_large_int": 0.6,
        "has_float": 0.7,
        "has_empty_list": 0.5,
        "has_empty_str": 0.5,
        "has_none": 0.6,
        "has_unicode": 0.8,
        "has_exception": 0.8,
        "has_whitespace_edge": 0.7,
    }
    score = 0.0
    for k, wt in w.items():
        score += wt * float(row.get(k, 0) or 0)
    return round(score, 2)

def bucket(score: float) -> str:
    if score < 6.0: return "Easy"
    if score < 12.0: return "Medium"
    if score < 18.0: return "Hard"
    return "Challenging"

def process(input_path: Path, out_path: Path):
    rows = []
    with input_path.open('r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            task_id = obj.get('task_id') or obj.get('id') or ''
            entry_point = obj.get('entry_point') or ''
            prompt = to_text(obj.get('prompt',''))
            sol = to_text(obj.get('canonical_solution',''))
            tests = to_text(obj.get('test',''))

            feats = {}
            feats.update(ast_features(sol, entry_point))
            feats.update(prompt_features(prompt))
            feats.update(test_features(tests))

            row = {'task_id': task_id, 'entry_point': entry_point, **feats}
            row['difficulty_score'] = score_row(row)
            row['difficulty_bucket'] = bucket(row['difficulty_score'])
            rows.append(row)

    fields = list(rows[0].keys()) if rows else []
    import csv as _csv
    with out_path.open('w', newline='', encoding='utf-8') as csvfile:
        writer = _csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True, type=Path)
    ap.add_argument('--out', required=True, type=Path)
    args = ap.parse_args()
    process(args.input, args.out)
    print(f"[ok] Wrote: {args.out}")

if __name__ == '__main__':
    main()
