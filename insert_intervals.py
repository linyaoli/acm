# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        n = len(intervals)
        i = 0
        while i < n:
            if newInterval.end < intervals[i].start:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval.start > intervals[i].end:
                i += 1
                continue
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                del intervals[i]
                n -= 1

        intervals.append(newInterval)
        return intervals


sol = Solution()
a = [Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10),Interval(12,16)]
#a = [Interval(3,5),Interval(12,15)]
#a = [Interval(1,5)]
b = sol.insert(a, Interval(2,3))

for i in b:
    print i.start, i.end
