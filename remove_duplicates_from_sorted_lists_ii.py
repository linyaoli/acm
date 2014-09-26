# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        # saber protects us from None list.
        saber = ListNode(-999)
        saber.next = head

        if head is None:
            return None
        if head.next is None:
            return head
        # if the val of two near nodes are the same?
        same = False
        ptr = saber.next
        pre_ptr = saber
        while ptr.next is not None:
            if ptr.next.val != ptr.val:
                if same is True:
                    same = False
                    pre_ptr.next = ptr.next
                else:
                    pre_ptr = pre_ptr.next
            else:
                same = True
            ptr = ptr.next
        if same is True:
            pre_ptr.next = ptr.next
        return saber.next
