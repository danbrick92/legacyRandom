# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(val=-1) 
        node = first
        while (list1 is not None) or (list2 is not None):
            if list1 is None:
                node.next = list2
                break
            elif list2 is None:
                node.next = list1
                break
            elif list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        return first.next
