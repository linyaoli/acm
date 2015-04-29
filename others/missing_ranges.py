"""
Question:
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return ["2", "4->49", "51->74", "76->99"]
Example Questions Candidate Might Ask:
Q: What if the given array is empty?
A: Then you should return ["0->99"] as those ranges are missing.
Q: What if the given array contains all elements from the ranges? A: Return an empty list, which means no range is missing.

"""
class Solution :
    def missingRange(self, arr):
        if arr == []:
            return ["0->99"]
        arr.append(100)
        ret = []
        last = arr[0]
        for i in xrange(1, len(arr)):
            if arr[i] - last > 2:
                ret.append(str(last + 1) + "->" + str(arr[i] - 1))
            elif arr[i] - last > 1:
                ret.append(str(last + 1))
            else:
                pass
            last = arr[i]

        return ret


sol = Solution()
print sol.missingRange([0,1,3,50,75])
print sol.missingRange([])
print sol.missingRange(range(100))
print sol.missingRange(range(0, 100,4))
