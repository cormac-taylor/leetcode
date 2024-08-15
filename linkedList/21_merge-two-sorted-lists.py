from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Time complexity: O(min(n, m))
    Space complexity: O(1)
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = ListNode(-101, None)
        tail = head

        ptr1 = list1
        ptr2 = list2
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next

        if ptr1:
            tail.next = ptr1
        else:
            tail.next = ptr2        
        return head.next
