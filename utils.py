def quality_label(score):
    if score >= 85:
        return "Excellent"
    elif score >= 70 and score <= 84:
        return "Good"
    elif score >= 50 and score <= 69:
        return "Fair"
    else:
        return "Poor"

def normalize_quality(score, current_max=100):
    normalized = (score / current_max) * 100
    return round(normalized, 2)

def compute_sleep_score(duration, quality_score):
    duration_factor = min(duration / 8.0, 1.0) * 60
    quality_factor = quality_score * 0.4
    total_score = duration_factor + quality_factor
    return round(min(total_score, 100), 2)





