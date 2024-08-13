from collections import defaultdict

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        netCharOccurrences = defaultdict(int)
        for i in range(len(s)):
            netCharOccurrences[s[i]] += 1
            netCharOccurrences[t[i]] -= 1

        for x in netCharOccurrences.values():
            if x != 0:
                return False
        return True