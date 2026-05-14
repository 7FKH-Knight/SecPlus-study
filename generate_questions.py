#!/usr/bin/env python3
"""Combine per-domain question banks into questions.json."""
import json
import sys
import os
import importlib

sys.path.insert(0, os.path.dirname(__file__))

all_questions = []
for domain_num, mod_name, var_name in [
    (1, "q_domain1", "questions"),
    (2, "q_domain2", "questions"),
    (3, "q_domain3", "questions"),
    (4, "q_domain4", "questions"),
    (5, "q_domain5", "DOMAIN5_QUESTIONS"),
]:
    mod = importlib.import_module(mod_name)
    qs = getattr(mod, var_name)
    all_questions.extend(qs)

# Validate
errors = []
seen_ids = set()
for q in all_questions:
    qid = q.get("id")
    if qid in seen_ids:
        errors.append(f"Duplicate ID: {qid}")
    seen_ids.add(qid)
    if q.get("correct_answer") not in "ABCD":
        errors.append(f"ID {qid}: invalid correct_answer '{q.get('correct_answer')}'")
    if set(q.get("options", {}).keys()) != {"A", "B", "C", "D"}:
        errors.append(f"ID {qid}: options keys wrong")
    required_exp = {"correct", "A", "B", "C", "D"}
    if set(q.get("explanations", {}).keys()) != required_exp:
        errors.append(f"ID {qid}: explanation keys wrong")

if errors:
    print("ERRORS found:")
    for e in errors:
        print(" ", e)
    sys.exit(1)

output = {"questions": all_questions}
out_path = os.path.join(os.path.dirname(__file__), "questions.json")
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

by_domain = {}
for q in all_questions:
    d = q["domain"]
    by_domain[d] = by_domain.get(d, 0) + 1

print(f"Generated {len(all_questions)} questions into questions.json")
for d in sorted(by_domain):
    print(f"  Domain {d}: {by_domain[d]} questions")
