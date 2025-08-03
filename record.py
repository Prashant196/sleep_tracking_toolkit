from utils import compute_sleep_score, quality_label

class DailySleepRecord():
    def __init__(self, date, segments):
        self.date = date
        self.segments = segments
    
    def average_quality(self):
        # for _ , quality in self.segments:
        #     q1 = self.segments[0][1]
        #     q2 = self.segments[1][1]
        #     total = q1 + q2
        #     round_avg = round(total / len(self.segments), 2)
        # print(f"Average is {round_avg}")
        total = 0
        for _ , quality in self.segments:
            total += quality
        avg = total / len(self.segments)
        return round((avg),2)
     
    def total_quality(self):
        total = 0
        for _ , quality in self.segments:
            total += quality
        return round(total, 2)
    
    def total_duration(self):
        total = 0
        for duration, _ in self.segments:
            total += duration
        return round(total, 2)
        
    def is_restful(self, duration_threshold = 7.0, quality_threshold = 75):
            # for x in range(len(records)):
            # test = records[x]
            # print(f"{records[x]} and {test}")
            # if (self.total_duration(records[x]) > duration_threshold and self.average_quality(records[x]) > quality_threshold):
            #     # print(f"Total Duration is {DailySleepRecord.total_duration(records[x])}")
            #     # print(f"Avg Quality is {DailySleepRecord.total_quality(records[x])}")
            #     print(f"The {self.date(records[x])} day was restful : {True}")
            #     # return True
            # else:
            #     print(f"The {self.date(records[x])} day was restful : {False}")
            #     return False
            
        return  all(duration >= duration_threshold and quality >= quality_threshold for duration, quality in self.segments)
        
    def average_sleep_score(self):
        sleep_score = [compute_sleep_score(duration, quality_score) for duration, quality_score in self.segments]
        return round(sum(sleep_score)/len(self.segments), 2)
        
        
    def summary(self):
        return {
             'date': self.date,
             'avg_quality' : self.average_quality(),
             'total_duration': self.total_duration(),
             'avg_sleep_score': self.average_sleep_score(),
             'quality_label': quality_label(self.average_sleep_score())
        }
        
# D1 = DailySleepRecord('2025-02-01', [(3.5, 85), (2.5, 80)])
# print(f"Date : {}")
# print(f"Segments : {self.segments}")
# print(f"Average Quality of Sleep is : {D1.average_quality()}")
# print(f"Total Duration is : {D1.total_duration()}")
# print(f"Total Quality Score: {D1.total_quality()}")
# # DailySleepRecord.is_restful(records[0])
# print(f"{DailySleepRecord.is_restful(records[0])}")
