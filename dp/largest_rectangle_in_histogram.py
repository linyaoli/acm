class Solution:
    # @param height, a list of integer
    # @return an integer
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
                print stack, i, area,
                cur = stack.pop()
                width = i if stack == [] else i - (stack[-1] + 1)
                print height[cur], width
                area = max(area, height[cur] * width)

        return area

sol = Solution()
print sol.largestRectangleArea([2, 4,5,3,4,5])
