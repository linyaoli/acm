# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
# Input: The root of a Binary Search Tree like this:
#              5
#            /   \
#           2     13
#
# Output: The root of a Greater Tree like this:
#             18
#            /   \
#          20     13
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {TreeNode}
def convert_bst(root)
  @sum = 0
  dfs(root)
  return root
end

def dfs(root)
  return nil if root.nil?
  dfs(root.right)
  root.val += @sum
  @sum = root.val
  dfs(root.left)
end
