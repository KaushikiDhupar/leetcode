# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:return None
        prev=ListNode(0)

        prev.next=head
        fast,slow=head,prev
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return prev.next


