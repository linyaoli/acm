"""
Given a singly linked list L: L0 -> L1 -> .. -> Ln-1 -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 ->...

"""
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head
        # go to the mid of listnode
        slow = head
        fast = head
        while True:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            if not fast:
                break
            slow = slow.next
        
        tail = self.reverse(slow)
        slow.next = None
        self.merge(head, tail)

    def reverse(self, head):
        cur = head
        pre = head.next
        while pre:
            tmp = pre.next
            pre.next = cur
            cur = pre
            pre = tmp
        return cur

    def merge(self, head1, head2):
        while head1 and head2 and head1 != head2:
            tmp = head2.next
            head2.next = head1.next
            head1.next = head2
            head1 = head2.next
            head2 = tmp
