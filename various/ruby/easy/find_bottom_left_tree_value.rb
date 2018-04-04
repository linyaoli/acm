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
# https://leetcode.com/problems/find-bottom-left-tree-value/#/description
def find_bottom_left_value(root)
  level_list = [root]
  tmp = []
  first_node = root
  while level_list != []
    node = level_list.shift
    tmp << node.left
    tmp << node.right

    if level_list == []
      tmp.compact!
      break if tmp == []
      level_list = tmp
      first_node = tmp[0]
      tmp = []
    end
  end

  first_node.val
end
