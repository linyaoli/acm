# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
# https://leetcode.com/problems/combination-sum-iii/#/description
def combination_sum3(k, n)
  @k = k
  @n = n
  result = []
  permutate(1, result, [])
  result
end

def permutate(i, result, solution)
  if sum(solution) > @n
    return
  elsif sum(solution) == @n && solution.size == @k
    sorted_solution = solution.sort
    result << sorted_solution if !result.include?sorted_solution
  else
    for j in i..9
      solution << j
      permutate(j+1, result, solution)
      solution.pop
    end
  end
end

def sum(arr)
  arr.inject(0, :+)
end

p combination_sum3(3,9)
