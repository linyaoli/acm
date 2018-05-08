# https://leetcode.com/problems/house-robber-iii/description/
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
def rob(root)
  traverse(root).max
end

def traverse(node)
  return 0, 0 if node.nil?
  l1, l2 = traverse(node.left)
  r1, r2 = traverse(node.right)

  val1 = node.val + l2 + r2
  val2 = [l1, l2].max + [r1, r2].max

  return val1, val2 
end
