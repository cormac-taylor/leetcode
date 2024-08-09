class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = {}
        maxLen, indexOfLastDup = 0, -1
        for i in range(len(s)):
            if s[i] in seenChars:
                indexOfLastDup = max(indexOfLastDup, seenChars[s[i]])
            seenChars[s[i]] = i
            maxLen = max(maxLen, i - indexOfLastDup)
        return maxLen