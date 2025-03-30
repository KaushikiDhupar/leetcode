

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # Dummy node to start the new list
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 (0 if None)
            val2 = l2.val if l2 else 0  # Get value from l2 (0 if None)
            
            total = val1 + val2 + carry  # Add both values and carry
            carry = total // 10  # Update carry for next addition
            current.next = ListNode(total % 10)  # Create new node with last digit
            
            # Move to next nodes
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next  # Return head of the result list
