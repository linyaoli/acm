# https://leetcode.com/problems/maximum-binary-tree/description/
#
# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

# @param {Integer[]} nums
# @return {TreeNode}
def construct_maximum_binary_tree(nums)
  return nil if nums.size == 0
  v, i = index_of_max(nums)
  cur = TreeNode.new(v)

  cur.left = construct_maximum_binary_tree(nums[0..i-1]) if i >= 1
  cur.right = construct_maximum_binary_tree(nums[i+1..-1]) if i < nums.size - 1
  cur
end

def index_of_max(nums)
  m = nums.max
  return m, nums.find_index(m)
end

p construct_maximum_binary_tree([3,2,1])
