from utils import compute_sleep_score

def overall_average_duration(records):
    all_durations = [duration for r in records for duration, _ in r.segments]
    if not all_durations:
        return 0
    return round(sum(all_durations) / len(all_durations), 2)


def best_sleep_day(records):
    if not records:
        return None
    best_record = max(records, key=lambda r: r.average_sleep_score())
    return best_record.date


def detect_under_sleep_days(records, threshold):
    under_days = []
    for record in records:
        for duration, _ in record.segments:
            if duration < threshold:
                under_days.append(record.date)
                break  # Only add once per day
    return under_days


def detect_spike(durations, *, threshold=2):    
    for i in range(1, len(durations)):
        if abs(durations[i] - durations[i-1]) >= threshold:
            return True
    return False


def duration_trend(durations):
    if len(durations) < 2:
        return []
    trend = []
    for i in range(1, len(durations)):
        if durations[i] > durations[i-1]:
            trend.append("up")
        elif durations[i] < durations[i-1]:
            trend.append("down")
        else:
            trend.append("same")
    return trend


def average_sleep_score_across_days(records):
    scores = []
    for r in records:
        for duration, quality in r.segments:
            score = compute_sleep_score(duration, quality)
            scores.append(score)
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)
