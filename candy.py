class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        N = len(ratings)
        candies = [1] * N
        i = 1
        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1
            elif ratings[i - 1] > ratings[i]:
                candies[i] = candies[i - 1] - 1
            else:
                candies[i] = 1

            if i < len(ratings) - 1 and ratings[i] < ratings[i-1] and ratings[i] <= ratings[i+1]:
                self.adjust(ratings, candies, i)

        if N >= 2:
            if ratings[-1] < ratings[-2]:
                self.adjust(ratings, candies, len(ratings)-1)

        return sum(candies)

    def adjust(self, ratings, candies, n):
        k = n
        diff = 1 - candies[k]
        while k > 0 and ratings[k - 1] > ratings[k]:
            candies[k] = candies[k] + diff
            k -= 1
        if diff > 0:
            candies[k] += diff

sol = Solution()
print sol.candy([1])
