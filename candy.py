class Solution:
    def candy(self, ratings):
        N = len(ratings)
        candies = [1] * N
        for i in range(1, N, 1):
            if ratings[i - 1] > ratings[i]:
                candies[i] = candies[i] - 1
        total = 0
        min = candies[0]
        for elem in candies:
            total = total + elem
            if min > elem:
                min = elem
        total = total + (1 - min) * N

        return total

sol = Solution()
ratings = [1, 2]
print sol.candy(ratings)
