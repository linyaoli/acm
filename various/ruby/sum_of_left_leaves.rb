# https://leetcode.com/problems/sum-of-left-leaves/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def sum_of_left_leaves(root)
  return dfs(root)
end

def dfs(root)
  return 0 if root.nil?
  result = dfs(root.left) + dfs(root.right)
  result += root.left.val if !root.left.nil? && is_leaf(root.left)

  return result
end

def is_leaf(node)
  return true if node.left.nil? && node.right.nil?
  false
end
