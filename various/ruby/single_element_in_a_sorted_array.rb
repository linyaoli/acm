# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# @param {Integer[]} nums
# @return {Integer}
def single_non_duplicate(nums)
  left = 0
  right = nums.size - 1
  while left <= right 
    mid = (left + right) / 2
    case nums[mid]
    when nums[mid-1]
      if (mid - left + 1) % 2 == 1
        right = mid - 2
      else
        left = mid + 1
      end
    when nums[mid+1]
      if (right - mid + 1) % 2 == 1
        left = mid + 2
      else
        right = mid - 1
      end
    else
      return nums[mid]
    end
  end
end

p single_non_duplicate([1,1,2,3,3,4,4,8,8])
p single_non_duplicate([3,3,7,7,10,11,11])
p single_non_duplicate([1, 1, 2, 2, 4, 4, 5, 5,9])
