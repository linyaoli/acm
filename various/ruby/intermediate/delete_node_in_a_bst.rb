# https://leetcode.com/problems/delete-node-in-a-bst/description/
# # Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} key
# @return {TreeNode}
def delete_node(root, key)
  @key = key
  dummy = TreeNode.new(10000)
  dummy.left = root
  trav(dummy)

  return dummy.left 
end

def trav(node)
  return if node.nil?
  if node.left && node.left.val == @key 
    if node.left.left
      rotate(node.left)
      node.left = node.left.left
    elsif node.left.right
      node.left = node.left.right
    else
      node.left = nil
    end
  elsif node.right && node.right.val == @key 
    if node.right.left
      rotate(node.right)
      node.right = node.right.left
    elsif node.right.right
      node.right = node.right.right
    else
      node.right = nil
    end
  else
    if @key > node.val
      trav(node.right)
    elsif @key < node.val
      trav(node.left)
    end
  end
end

def rotate(node)
  tmp = node.left
  while tmp.right != nil
    tmp = tmp.right
  end
  tmp.right = node.right
end
