#!/usr/bin/env python3
import json, re, csv, argparse, sys
from pathlib import Path
from typing import Dict, Any, Iterable

PATTERNS = {
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

CATEGORIES_READABLE = {
    "has_negative": "Negatives",
    "has_zero": "Zero",
    "has_large_int": "Large integers",
    "has_float": "Floats/Scientific",
    "has_empty_list": "Empty list",
    "has_empty_str": "Empty string",
    "has_none": "None/null",
    "has_unicode": "Unicode",
    "has_exception": "Exceptions",
    "has_whitespace_edge": "Whitespace/Escapes",
}

def to_text(x):
    if isinstance(x, list):
        return "\n\n".join(str(i) for i in x)
    return str(x or "")

def count_asserts(s: str) -> int:
    import re
    return len(re.findall(r"(?<![A-Za-z_])assert(?![A-Za-z_])", s))

def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            try:
                yield json.loads(line)
            except Exception as e:
                sys.stderr.write(f"[warn] Skipping malformed line: {e}\n")

def analyze(input_path: Path):
    rows = []
    for obj in iter_jsonl(input_path):
        task_id = obj.get("task_id") or obj.get("id") or ""
        entry_point = obj.get("entry_point") or ""
        tests = to_text(obj.get("test", ""))
        num_asserts = count_asserts(tests)
        flags = {}
        for k, pat in PATTERNS.items():
            flags[k] = bool(pat.search(tests))
        rows.append({
            "task_id": task_id,
            "entry_point": entry_point,
            "num_asserts": num_asserts,
            **flags
        })
    return rows

def write_csv(rows, out_path: Path):
    fields = ["task_id", "entry_point", "num_asserts", *PATTERNS.keys()]
    with out_path.open("w", newline="", encoding="utf-8") as csvfile:
        import csv as _csv
        writer = _csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def write_markdown(rows, md_path: Path):
    totals = {k: 0 for k in PATTERNS.keys()}
    for r in rows:
        for k in PATTERNS.keys():
            totals[k] += int(bool(r.get(k)))
    n = len(rows) or 1
    lines = []
    lines.append("# HumanEval Gap Report\n")
    lines.append("## Coverage summary by category\n")
    lines.append("| Category | Covered | Coverage |")
    lines.append("|---|---:|---:|")
    for k, v in totals.items():
        pct = 100.0 * v / n
        lines.append(f"| {CATEGORIES_READABLE[k]} | {v}/{n} | {pct:.1f}% |")
    lines.append("\n## Per-task coverage (excerpt)\n")
    lines.append("`num_asserts` alongside boolean flags per category.\n")
    for r in rows[:20]:
        covered = [CATEGORIES_READABLE[k] for k in PATTERNS if r.get(k)]
        missing = [CATEGORIES_READABLE[k] for k in PATTERNS if not r.get(k)]
        lines.append(f"### {r.get('task_id','')} (`{r.get('entry_point','')}`)")
        lines.append(f"- asserts: **{r.get('num_asserts',0)}**")
        lines.append(f"- covered: {', '.join(covered) if covered else '—'}")
        lines.append(f"- missing: {', '.join(missing) if missing else '—'}\n")
    md_path.write_text("\n".join(lines), encoding="utf-8")

def print_summary(rows):
    totals = {k: 0 for k in PATTERNS.keys()}
    for r in rows:
        for k in PATTERNS.keys():
            totals[k] += int(bool(r.get(k)))
    n = len(rows) or 1
    print("Coverage summary by category")
    for k, v in totals.items():
        pct = 100.0 * v / n
        print(f"- {CATEGORIES_READABLE[k]:20s}: {v}/{n}  ({pct:.1f}%)")
    print("\nExamples of missing categories per task (first 10):")
    for r in rows[:10]:
        missing = [CATEGORIES_READABLE[k] for k in PATTERNS if not r.get(k)]
        print(f"* {r.get('task_id','')}: missing -> {', '.join(missing) if missing else '—'}")

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, type=Path, help="Path to HumanEval-like JSONL")
    ap.add_argument("--out", type=Path, help="Write CSV report here")
    ap.add_argument("--markdown", type=Path, help="Write Markdown summary here")
    ap.add_argument("--summary", action="store_true", help="Print summary to stdout")
    args = ap.parse_args()

    rows = analyze(args.input)

    if args.out:
        write_csv(rows, args.out)
        print(f"[ok] CSV written: {args.out}")
    if args.markdown:
        write_markdown(rows, args.markdown)
        print(f"[ok] Markdown written: {args.markdown}")
    if args.summary or (not args.out and not args.markdown):
        print_summary(rows)

if __name__ == "__main__":
    main()
