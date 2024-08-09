class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.translate(s) == self.translate(t)

    def translate(self, string: str):
        nextCharToMapTo = ord('a')
        map = {}
        res = ""
        for char in string:
            if char in map:
                res += map[char]
            else:
                map[char] = chr(nextCharToMapTo)
                res += map[char]
                nextCharToMapTo += 1
        return res