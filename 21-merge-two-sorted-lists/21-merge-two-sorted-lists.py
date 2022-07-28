# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode() #[0] 위치
        temp = head 
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next			
            elif l2.val <= l1.val:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return head.next
