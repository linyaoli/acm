# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
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
def min_diff_in_bst(root)
  @res = 10000
  @prev = -10000
  return inorder(root)
end

def inorder(root)
  inorder(root.left) if !root.left.nil?

  @res = [@res, root.val - @prev].min
  @prev = root.val

  inorder(root.right) if !root.right.nil?
  @res
end
