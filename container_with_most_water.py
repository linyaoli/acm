class Solution:
    # @return an integer
    def maxArea(self, height):
        max_contained = 0
        start = 0
        end = len(height) - 1

        while start < end:
            contained = min(height[start], height[end]) * (end - start)
            max_contained = max(max_contained, contained)
            # each time moves the lower board
            if height[start] <= height[end]:
                # if the left board is the lower one, the container's size is
                # determined by the left board. Whereever the right borad moves,
                # the current size is the maximum one.
                # Therefore, we dont have to move right board, instead, we move
                # the left board.
                start += 1
            else:
                end -= 1
        return max_contained
