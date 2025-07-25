# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode() #make a new linked list
        curr=dummy #traversal pointer

        carry=0
        while l1 or l2 or carry:
            #extract values
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            #perform addition and update value of carry for next iteration
            val=v1+v2+carry
            carry=val//10
            val=val%10 #extract unit value
            curr.next=ListNode(val) #place unit value in the new linked list
            #update pointers
            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        
        return dummy.next
        