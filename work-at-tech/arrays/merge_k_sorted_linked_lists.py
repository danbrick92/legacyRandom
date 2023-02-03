# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Start
        vals = []
        node = ListNode(val = -1)
        first = node
        
        # Populate initial vals
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(vals, (lists[i].val, i))

        # Iterate
        while vals:
            _, i = heapq.heappop(vals)
            # Set new values
            node.next = lists[i]
            lists[i] = lists[i].next
            # Add to list and sort
            if lists[i] is not None:
                heapq.heappush(vals, (lists[i].val, i))
            node = node.next
        return first.next