# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
  return true if head.nil? || head.next.nil?
  # find the start node of right part
  l = head
  r = head.next
  @odd = false
  while true 
    if r.next == nil
      r = l.next
      l = head
      break
    end
    if r.next.next == nil
      r = l.next.next
      l = head
      @odd = true
      break
    end
    l = l.next
    r = r.next.next
  end
  @r = r

  return traverse(l)
end

def traverse(node)
  if (@odd && node.next.next == @r) || (!@odd && node.next == @r)
    if node.val == @r.val
      return true
    else
      return false
    end
  end

  return false if traverse(node.next) == false

  @r = @r.next
  if node.val == @r.val
    return true
  else
    return false
  end
end
