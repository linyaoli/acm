# https://leetcode.com/problems/binary-tree-pruning/description/
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
def prune_tree(root)
  return nil if root.nil?
  trav(root)
  return root
end

def trav(root)
  return false if root.nil?
  l = trav(root.left)
  root.left = nil if l == false

  r = trav(root.right)
  root.right = nil if r == false

  if root.val == 1 || l == true || r == true
    return true
  else
    return false
  end
end
