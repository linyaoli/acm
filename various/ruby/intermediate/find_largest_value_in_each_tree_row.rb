# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer[]}
def largest_values(root)
  return [] if root.nil?
  queue = [root]
  res = []
  while queue.size > 0
    res << queue.map(&:val).max
    tq = []
    while queue.size > 0
      node = queue.shift
      tq << node.left unless node.left.nil?
      tq << node.right unless node.right.nil?
    end
    queue << tq
    queue.flatten!
  end

  res
end
