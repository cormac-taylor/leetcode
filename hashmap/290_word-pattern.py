class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()

        if len(pattern) != len(arr):
            return False

        patternMap = {}
        arrMap = {}

        for i in range(len(pattern)):
            if (pattern[i] in patternMap) != (arr[i] in arrMap):
                return False
            else:
                if pattern[i] in patternMap and patternMap[pattern[i]] != arrMap[arr[i]]:
                    return False
                patternMap[pattern[i]] = i
                arrMap[arr[i]] = i
        return True