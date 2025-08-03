from utils import compute_sleep_score

def overall_average_duration(records):
    if not records:
        return 0
    total = 0
    count = 0
    for record in records:
        for duration, _ in record.segments:
            total += duration
            count += 1
    return round(total / count, 2) if count else 0

def best_sleep_day(records): 
    if not records:
        return 0
    else:
        best_record = records[0]
        highest_score = best_record.average_sleep_score()
        for record in records[1:]:
            score = record.average_sleep_score()
            if score > highest_score:
                best_record = record
                highest_score = score
        return best_record.date  
    
def detect_under_sleep_days(records, threshold):
    under_days = []
    records.date
    for record in records :
         if any(duration < threshold for duration, _ in record.segments):
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
    for record in records:
        for duration, quality in record.segments:
            score = compute_sleep_score(duration, quality)
            scores.append(score)
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 2)
