# https://leetcode.com/problems/subtree-of-another-tree/description/
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} s
# @param {TreeNode} t
# @return {Boolean}
def is_subtree(s, t)
  return false if s.nil?
  res = if s.val == t.val
    check(s, t)
  end

  return true if res
  return is_subtree(s.left, t) || is_subtree(s.right, t) 
end

def check(s, t)
  return true if s.nil? && t.nil?

  if (s.nil? || t.nil?) || s.val != t.val
    return false
  else
    return check(s.left, t.left) && check(s.right, t.right)
  end
end
