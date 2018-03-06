# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Float[]}
def average_of_levels(root)
  queue = [root]
  result = []

  while queue != []
    nodes_on_same_level = []
    val = 0
    n = 0
    while queue != []
      node = queue.shift
      val += node.val
      n += 1
      nodes_on_same_level << node.left if !node.left.nil?
      nodes_on_same_level << node.right if !node.right.nil?
    end

    result << val * 1.0 / n
    queue << nodes_on_same_level
    queue.flatten!
  end

  result
end
