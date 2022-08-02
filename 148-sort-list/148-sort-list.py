# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		res = []
		while head:
			res.append(head.val)
			head = head.next

		res.sort()

		ans = ListNode()
		temp = ans
		for i in res:
			ans.next = ListNode(i)
			ans = ans.next
		return temp.next
        
        