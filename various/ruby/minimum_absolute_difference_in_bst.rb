# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
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
def get_minimum_difference(root)
  @min = 10000
  @prev = nil

  return inorder(root)
end

def inorder(root)
  return @min if root.nil?
  inorder(root.left)

  if !prev.nil?
    @min = [@min, root.val - prev].min
  end

  prev = root.val
  inorder(root.right)

  return @min
end
