from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Time complexity: O(max(n, m))
    Space complexity: O(max(n, m))
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1, None)
        tail = head
        carry = 0

        ptr1 = l1
        ptr2 = l2
        while ptr1 or ptr2:
            num1 = ptr1.val if ptr1 else 0
            num2 = ptr2.val if ptr2 else 0

            sum = num1 + num2 + carry
            carry = sum // 10
            tail.next = ListNode(sum % 10, None)
            tail = tail.next

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        if carry == 1:
            tail.next = ListNode(carry, None)
        return head.next
