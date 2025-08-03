from .utils import compute_sleep_score, quality_label

class DailySleepRecord:
    def __init__(self,date,segments):
        self.date = date
        self.segments = segments

    def average_quality(self):
        if not self.segments:
            return 0
        else:
            total = 0 
            for _, quality in self.segments:
                total += quality
                avg = round(total / len(self.segments),2)
            return avg


    def total_duration(self):
        total = 0 
        for duration, _ in self.segments:
            total += duration
        return round(total,2)  

    def is_restful(self, duration_threshold = 7, quality_threshold = 75):
        total_d = 0
        for duration, _ in self.segments:
            total_d += duration
        
        total_q = 0
        for _, quality in self.segments:
            total_q += quality

        for duration, quality in self.segments:
            if (total_d >= duration_threshold and total_q >= quality_threshold):
                return True
            else:
                return False
    
    def avg_sleep_score(self):
        if not self.segments:
            return 0
        else:
            score = [compute_sleep_score(duration,quality)
                for duration, quality in self.segments
            ]
            return round(sum(score)/len(score),2)


    def summary(self):
        avg_quality = self.average_quality()
        total_dur = self.total_duration()
        avg_score = self.avg_sleep_score()
        label = quality_label(avg_score)
        return {
            'date': self.date,
            'avg_quality': avg_quality,
            'total_duration': total_dur,
            'avg_sleep_score': avg_score,
            'quality_label': label
        }


records = [
    DailySleepRecord("2025-04-01", [(6.5, 70), (1.2, 60)]),
    DailySleepRecord("2025-04-02", [(7.8, 82)]),
    DailySleepRecord("2025-04-03", [(5.5, 50), (0.5, 40)]),
    DailySleepRecord("2025-04-04", [(8.0, 90)]),
    DailySleepRecord("2025-04-05", [(4.2, 35), (2.0, 60)]),
    DailySleepRecord("2025-04-06", [(7.0, 78), (1.0, 70)]),
    DailySleepRecord("2025-04-07", [(6.0, 68)]),
]

print("===== DAILY SUMMARIES =====")
for r in records:
    print(f"Date: {r.date}")
    summary = r.summary()
    print(summary)

print(f"\nRestful? {records[2].is_restful()}")
print()
