# @param {Integer[]} find_nums
# @param {Integer[]} nums
# @return {Integer[]}
def next_greater_element(find_nums, nums)
  mapper = {}
  nums.each_with_index do |n, i|
    mapper[n] = i
  end
  result = []
  find_nums.each do |n|
    i = mapper[n] + 1
    while i < nums.size
      if nums[i] > n
        result << nums[i]
        break
      end
      i += 1
    end

    result << -1 if i == nums.size
  end

  result
end

p next_greater_element([4,1,2],[1,3,4,2])
