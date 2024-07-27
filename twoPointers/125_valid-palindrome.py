class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
            elif s[left].isalnum():
                left -= 1
            elif s[right].isalnum():
                right += 1
            left += 1
            right -= 1
        return True