package main

import (
  "fmt"
  "sort"
)

// https://leetcode.com/problems/two-sum/description/ 

func twoSum(nums []int, target int) []int {
  lIdx := 0
  rIdx := len(nums) - 1
  actual := make([]int, len(nums), len(nums))
  copy(actual, nums)
  sort.Ints(nums)

  for (lIdx < rIdx) {
    actual := nums[lIdx] + nums[rIdx]
    if (actual < target) {
      lIdx += 1
    } else if (actual > target) {
      rIdx -= 1
    } else {
      break
    }
  }

  left := -1
  right := -1

  for i, v := range actual {
    if v == nums[lIdx] && left == -1 {
      left = i
    } else if v == nums[rIdx] {
      right = i
    }
  }

  if left < right {
    return []int{left, right}
  } else {
    return []int{right, left}
  }
}

func main() {
  //res := twoSum([]int{2, 7, 11, 15}, 9)
  res := twoSum([]int{2, 5, 5, 11}, 10)
  fmt.Println(res)
}
