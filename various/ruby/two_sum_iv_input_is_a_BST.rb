# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} k
# @return {Boolean}
def find_target(root, k)
  @map = {}
  return dfs(root, k)
end

def dfs(root, k)
  return false if root.nil?
  return true if !@map[k - root.val].nil?
  @map[root.val] = true
  return dfs(root.left, k) || dfs(root.right, k)
end
