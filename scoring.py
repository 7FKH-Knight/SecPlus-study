DOMAIN_NAMES = {
    1: "General Security Concepts",
    2: "Threats, Vulnerabilities & Mitigations",
    3: "Security Architecture",
    4: "Security Operations",
    5: "Security Program Management & Oversight",
}

DOMAIN_WEIGHTS = {1: 0.12, 2: 0.22, 3: 0.18, 4: 0.28, 5: 0.20}


def scale_score(raw_correct: int, total: int = 90) -> int:
    if total == 0:
        return 100
    pct = raw_correct / total
    if pct <= 0.72:
        scaled = 100 + (pct / 0.72) * 650
    else:
        scaled = 750 + ((pct - 0.72) / 0.28) * 150
    return round(min(900, max(100, scaled)) / 10) * 10


def domain_breakdown(answers: list) -> dict:
    """
    answers: list of dicts with keys domain, is_correct.
    Returns {domain_int: {"correct": n, "total": n, "pct": float}}.
    """
    stats = {d: {"correct": 0, "total": 0} for d in range(1, 6)}
    for a in answers:
        d = a["domain"]
        if d in stats:
            stats[d]["total"] += 1
            if a["is_correct"]:
                stats[d]["correct"] += 1
    for d, v in stats.items():
        v["pct"] = round(v["correct"] / v["total"] * 100, 1) if v["total"] else 0
        v["name"] = DOMAIN_NAMES[d]
    return stats


def select_exam_questions(all_ids_by_domain: dict, total: int = 90) -> list:
    """
    Proportionally sample question IDs by domain weight.
    all_ids_by_domain: {domain_int: [id, ...]}
    Returns flat list of question IDs.
    """
    import random
    selected = []
    remaining = total
    domains = list(DOMAIN_WEIGHTS.items())

    for i, (domain, weight) in enumerate(domains):
        if i == len(domains) - 1:
            count = remaining
        else:
            count = round(total * weight)
        pool = all_ids_by_domain.get(domain, [])
        count = min(count, len(pool))
        selected.extend(random.sample(pool, count))
        remaining -= count

    random.shuffle(selected)
    return selected
