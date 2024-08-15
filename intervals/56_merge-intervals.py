from typing import List

class Solution:
    """
    Time complexity: O(n log(n))
    Space complexity: O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        resPtr = 0
        intervalPtr = 1
        while intervalPtr < len(intervals):
            if res[resPtr][1] >= intervals[intervalPtr][0]:
                res[resPtr][1] = max(res[resPtr][1], intervals[intervalPtr][1])
            else:
                res.append(intervals[intervalPtr])
                resPtr += 1
            intervalPtr += 1
        return res
            