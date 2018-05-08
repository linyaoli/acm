# https://leetcode.com/problems/path-sum-iii/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} sum
# @return {Integer}
def path_sum(root, sum)
  return 0 if root.nil?
  @sum = sum
  @count = 0
  traverse(root, [])

  @count
end

def traverse(node, sums)
  return if node.nil?
  sums.map!{ |s| s + node.val }
  sums << node.val
  @count += sums.count(@sum)
  traverse(node.left, sums)
  traverse(node.right, sums)
  sums.pop
  sums.map!{ |s| s - node.val }
end
