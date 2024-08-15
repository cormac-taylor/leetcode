class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif stack == [] or c != stack.pop():
                return False
        return stack == []
