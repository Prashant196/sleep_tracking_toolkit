from sleep_tracking_toolkit.record import DailySleepRecord
from sleep_tracking_toolkit.analytics import *

# Sample records
records = [
    DailySleepRecord("2025-04-01", [(6.5, 70), (1.2, 60)]),
    DailySleepRecord("2025-04-02", [(7.8, 82)]),
    DailySleepRecord("2025-04-03", [(5.5, 50), (0.5, 40)]),
    DailySleepRecord("2025-04-04", [(8.0, 90)]),
    DailySleepRecord("2025-04-05", [(4.2, 35), (2.0, 60)]),
    DailySleepRecord("2025-04-06", [(7.0, 78), (1.0, 70)]),
    DailySleepRecord("2025-04-07", [(6.0, 68)]),
]

# Print summaries
print("===== DAILY SUMMARIES =====")
for r in records:
    print(f"Date: {r.date}")
    summary = r.summary()
    print(summary)

print(f"\nRestful? {records[2].is_restful()}")
print()

# Analytics
print("Overall average duration:", overall_average_duration(records))
print("Best sleep day (by score):", best_sleep_day(records))
print("Under sleep days:", detect_under_sleep_days(records))

durations = [r.total_duration() for r in records]

print("Total durations per day:", durations)
print("Sleep trend:", duration_trend(durations))
print("Spike detected?", detect_spike(durations))
print("Average sleep score across all days:", average_sleep_score_across_days(records))