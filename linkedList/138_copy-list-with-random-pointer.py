from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToNew = {}

        ptr = head
        while ptr:
            oldToNew[ptr] = Node(ptr.val, None, None)
            ptr = ptr.next

        ptr = head
        while ptr:
            oldToNew[ptr].next = oldToNew.get(ptr.next)
            oldToNew[ptr].random = oldToNew.get(ptr.random)
            ptr = ptr.next

        return oldToNew[head]