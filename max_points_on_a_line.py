class Solution:
    def maxPoints(self, points):
        max_count = 0
        count = 0
        radient = 0
        next_line = True
        for point in points:
            for _point in points:
                if next_line is True:
                    radient = (_point.y - point.y) / (_point.x - point.x)
                    next_line = False
                if point.x == _point.x and point.y == _point.y:
                    continue
                if next_line is False:
                    if radient == (_point.y - point.y) / (_point.x - point.x):
                        count = count + 1
            if count > max_count:
                max_count = count
            next_line = True

sol = Solution()
sol.maxPoints()



