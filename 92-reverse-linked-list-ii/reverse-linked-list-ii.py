# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        for i in range(left-1):
            prev=prev.next
        curr=prev.next
        for i in range(right-left):
            temp=prev.next
            prev.next=curr.next
            curr.next=curr.next.next
            prev.next.next=temp

        return dummy.next
        