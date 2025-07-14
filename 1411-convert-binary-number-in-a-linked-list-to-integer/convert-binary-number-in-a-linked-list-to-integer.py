# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy=ListNode()
        dummy.next=head
        currsum=0
        counter=0
        while dummy.next:
            counter+=1
            dummy=dummy.next
        node=head
        for i in range(counter-1,-1,-1):
            currsum+=(node.val*2**i)
            node=node.next
        return currsum
    
        