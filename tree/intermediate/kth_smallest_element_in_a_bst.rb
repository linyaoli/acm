# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# # Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
  @res = k
  @number = 0
  helper(root)
  @number
end

def helper(node)
  helper(node.left) if !node.left.nil?
  @res -= 1
  if @res == 0
    @number = node.val
    return
  end
  helper(node.right) if !node.right.nil?
end
