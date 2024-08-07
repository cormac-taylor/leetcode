class Solution:
    """
    Time complexity: O(n), n is the lenth of t
    Space complexity: O(1)
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        subseqPtr = 0

        if s == "":
            return True

        for char in t:
            if s[subseqPtr] == char:
                subseqPtr += 1
            if subseqPtr == len(s):
                return True
        return False
