# https://leetcode.com/problems/reverse-linked-list/description/
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
def reverse_list(head)
    return head if head.nil? || head.next.nil?
    p = nil
    q = head
    r = head.next
    while !q.nil?
        q.next = p
        p = q
        q = r
        r = r.next if !r.nil?
    end
    
    p
end
