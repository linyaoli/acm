# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} t1
# @param {TreeNode} t2
# @return {TreeNode}
def merge_trees(t1, t2)
  trav(t1, t2, nil)
end

def trav(t1, t2, cur)
  cur = merge(t1, t2) if cur.nil?
  return if cur.nil?

  if t1.nil?
    cur.left = trav(nil, t2.left, cur.left)
    cur.right = trav(nil, t2.right, cur.right)
  elsif t2.nil?
    cur.left = trav(t1.left, nil, cur.left)
    cur.right = trav(t1.right, nil, cur.right)
  else
    cur.left = trav(t1.left, t2.left, cur.left)
    cur.right = trav(t1.right, t2.right, cur.right)
  end

  cur
end

def merge(n1, n2)
  if n1.nil? || n2.nil?
    return n1 || n2
  else
    return TreeNode.new(n1.val + n2.val)
  end
end
