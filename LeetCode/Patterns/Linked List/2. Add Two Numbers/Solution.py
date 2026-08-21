# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
    

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            # Get values from the nodes
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Add the digits and carry
            total = x + y + carry

            # Current digit
            digit = total % 10

            # Carry for next position
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move forward
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next