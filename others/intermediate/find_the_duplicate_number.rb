# https://leetcode.com/problems/find-the-duplicate-number/description/
# @param {Integer[]} nums
# @return {Integer}
# So I failed to solve this problem. The following idea is from leetcode
# discussions and it's quite easy to understand.
# At first the search space is numbers between 1 to n. Each time I select a number mid (which is the one in the middle) and count all the numbers equal to or less than mid. Then if the count is more than mid, the search space will be [1 mid] otherwise [mid+1 n]. I do this until search space is only one number.
# Let's say n=10 and I select mid=5. Then I count all the numbers in the array which are less than equal mid. If the there are more than 5 numbers that are less than 5, then by Pigeonhole Principle (https://en.wikipedia.org/wiki/Pigeonhole_principle) one of them has occurred more than once. So I shrink the search space from [1 10] to [1 5]. Otherwise the duplicate number is in the second half so for the next step the search space would be [6 10].
def find_duplicate(nums)
  low = 1
  high = nums.size - 1
  while low < high
    mid = low + (high - low) / 2
    count = 0
    nums.each do |n|
      count += 1if n <= mid
    end

    if count <= mid
      low = mid + 1
    else
      high = mid
    end
  end

  low
end
