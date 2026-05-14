from datetime import date, timedelta


def update_card(easiness: float, interval: int, repetitions: int, quality: int):
    """
    SM-2 algorithm. quality: 0=wrong, 4=correct.
    Returns (new_easiness, new_interval, new_repetitions, next_review_str).
    """
    new_easiness = max(
        1.3,
        easiness + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02),
    )

    if quality < 3:
        new_repetitions = 0
        new_interval = 1
    else:
        if repetitions == 0:
            new_interval = 1
        elif repetitions == 1:
            new_interval = 6
        else:
            new_interval = round(interval * easiness)
        new_repetitions = repetitions + 1

    next_review = (date.today() + timedelta(days=new_interval)).isoformat()
    return new_easiness, new_interval, new_repetitions, next_review


def quality_from_correct(is_correct: bool) -> int:
    return 4 if is_correct else 0
