from collections import defaultdict

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote): 
            return False

        magazineLetterCount = defaultdict(int)
        for c in magazine:
            magazineLetterCount[c] += 1

        for c in ransomNote:
            if magazineLetterCount[c] == 0:
                return False
            magazineLetterCount[c] -= 1
        return True
