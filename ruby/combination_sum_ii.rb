# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
# https://leetcode.com/problems/combination-sum-ii/#/description
def combination_sum2(candidates, target)
  result = []
  permutate(0, result, [], target, candidates)
  result
end

def permutate(i, result, solution, target, candidates)
  if sum(solution) > target
    return
  elsif sum(solution) == target
    sorted_solution = solution.sort
    result << sorted_solution if !result.include?sorted_solution
  else
    for j in i..candidates.size-1
      solution << candidates[j]
      permutate(j+1, result, solution, target, candidates)
      solution.pop
    end
  end
end

def sum(arr)
  arr.inject(0, :+)
end

p combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
p combination_sum2([1], 1)
p combination_sum2([1,2,3], 4)
