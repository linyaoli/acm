# https://leetcode.com/problems/diameter-of-binary-tree/description/
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
def diameter_of_binary_tree(root)
  @max = 0
  max_depth(root)
  return @max
end

def max_depth(root)
  return 0 if root.nil?
  left = max_depth(root.left)
  right = max_depth(root.right)

  @max = [@max, left + right].max

  return [left, right].max + 1
end
