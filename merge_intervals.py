# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        res = {}
        for item in intervals:
            if item.start not in res:
                res[item.start] = 1
            else:
                res[item.start] += 1
            if item.end not in res:
                res[item.end] = -1
            else:
                res[item.end] -= 1
        saber = 0#mark the intervals which share ranges.
        start = 0
        f_res = []
        tmp_res = []
        res = collections.OrderedDict(sorted(res.items()))
        for item in res:
            if start == 0:
                tmp_res.append(item)
                start = 1
            saber += res[item]
            if saber == 0:
                tmp_res.append(item)
                f_res.append(Interval(tmp_res[0], tmp_res[1]))
                tmp_res = []
                start = 0

        return f_res
