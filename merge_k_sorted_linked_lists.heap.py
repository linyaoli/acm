# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        head = None
        pre = head
        while len(heap) > 0:
            cur = heapq.heappop(heap)
            # cur -> tuple(node.val, node)
            if not head:
                head = cur[1]
                pre = head
            else:
                pre.next = cur[1]
            pre = cur[1]
            if cur[1].next:
                heapq.heappush(heap, (cur[1].next.val, cur[1].next))
        return head
