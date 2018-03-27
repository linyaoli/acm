# https://leetcode.com/problems/trim-a-binary-search-tree/description/
#
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} l
# @param {Integer} r
# @return {TreeNode}
def trim_bst(root, l, r)
  return nil if root.nil?
  if root.val < l
    return trim_bst(root.right, l ,r)
  elsif root.val > r
    return trim_bst(root.left, l, r)
  else
    root.left = trim_bst(root.left, l, r)
    root.right = trim_bst(root.right, l, r)

    return root
  end
end
