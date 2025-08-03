def quality_label(score):
    if score >= 85:
        return 'Excellent'
    elif score >= 70:
        return 'Good'
    elif score >= 50:
        return 'Fair'
    else:
        return 'Poor'

def normalize_quality(score, current_max=100):
    return round(score / current_max * 100, 2)

def compute_sleep_score(duration, quality_score):
    score = min(duration / 8.0, 1.0) * 60 + quality_score * 0.4
    return round(min(score, 100), 2)