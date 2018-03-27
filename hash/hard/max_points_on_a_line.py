# Definition for a point
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

# TODO DON'T MESS UP WITH INT AND FLOAT !
#      FIND THESE TIPS IN LINE 23 ~ 26
class Solution:
    def maxPoints(self, points):
        max_count = 0
        for idx1 in xrange(len(points)):
            dup = 1
            gradient_map = {0:0}
            for idx2 in xrange(len(points)):
                if idx1 == idx2:
                    continue
                if points[idx1].x == points[idx2].x and points[idx1].y == points[idx2].y:
                    #count duplicates
                    dup += 1
                    continue
                k = 0.0
                # while the line is vertical.
                if points[idx1].x - points[idx2].x == 0:
                    k = 999999999.0 # indicate k = Inf
                else:
                    k = (points[idx1].y - points[idx2].y) * 1.0 / (points[idx1].x - points[idx2].x)

                try:
                    gradient_map[k] += 1
                except:
                    gradient_map[k] = 1

            for kys in gradient_map.keys():
                if gradient_map[kys] + dup > max_count:
                    max_count = gradient_map[kys] + dup

        return max_count


sol = Solution()
pts1 = Point(84, 250)
pts2 = Point(0, 0)
pts3 = Point(1, 0)
pts4 = Point(0, -70)
pts5 = Point(0, -70)
pts6 = Point(1, -1)
pts7 = Point(21, 10)
pts8 = Point(42, 90)
pts9 = Point(-42, -230)

print sol.maxPoints([pts1, pts2,pts3,pts4,pts5,pts6,pts7,pts8,pts9])
