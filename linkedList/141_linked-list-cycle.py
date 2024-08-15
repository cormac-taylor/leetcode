from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            # fast checks all pointers so slow doesn't have to
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True