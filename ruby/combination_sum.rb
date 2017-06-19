# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
# https://leetcode.com/problems/combination-sum/#/description
def combination_sum(candidates, target)
  sol_set = []
  @target = target
  @candidates = candidates
  permutate(0, sol_set, [])
  sol_set
end

def permutate(i, res, sol)
  if sol.inject(0, :+) == @target
    res << sol.sort
  elsif sol.inject(0, :+) > @target || i == @candidates.size
    return
  else
    for j in i..@candidates.size-1
      sol << @candidates[j]
      permutate(j, res, sol)
      sol.pop
    end
  end
end)}
