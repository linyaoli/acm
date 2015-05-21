"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing all ones and return its area.

"""
class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]

        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j-1][i] + 1

        return max(self.largestRectangleArea(row) for row in m)


    def largestRectangleArea(self, height):
        #use a stack, maintain an increasing order in this stack by height.
        #while we meet a lower height, we calculate the rectangle made by current
        #height and previous heights, find the maximum one.
        stack, area, i = [], 0, 0
        height.append(0)

        while i < len(height):
            if stack == [] or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                cur = stack.pop()
                width = i if stack == [] else i - (stack[-1] + 1)
                area = max(area, height[cur] * width)

        return area
