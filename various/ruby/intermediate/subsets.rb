# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)
  res = []
  gen(nums, res, [], 0)
  res
end

def gen(nums, res, sol, i)
  res << sol.compact if !res.include?sol

  for j in i..nums.size - 1
    sol << nums[j]
    gen(nums, res, sol, j + 1)
    sol.pop
  end
end

p subsets([1,2,3])
