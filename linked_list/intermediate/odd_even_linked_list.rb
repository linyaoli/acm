# https://leetcode.com/problems/odd-even-linked-list/description/
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def odd_even_list(head)
  return head if head.nil?
  odd = head
  even = head.next
  even_head = even

  while even != nil && even.next != nil
    odd.next = even.next
    odd = odd.next

    even.next = odd.next
    even = even.next
  end

  odd.next = even_head

  return head
end
