class Solution:
    # @return an integer
    def maxArea(self, height):
        max_contained = 0
        start = 0
        end = len(height) - 1

        while start < end:
            contained = min(height[start], height[end]) * (end - start)
            max_contained = max(max_contained, contained)
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
        return max_contained

            
