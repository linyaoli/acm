class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):        
        stack, area, i = [], 0, 0
        height.append(0)
        while i < len(height):
            if stack == [] or height[i] > height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                curr = stack.pop()
                width = i if stack == [] else i - (stack[-1] + 1)
                area = max(area, height[curr] * width)
        return area
