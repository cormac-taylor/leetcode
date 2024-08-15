from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        numShots = 1
        upperBound = points[0][1]
        for x in range(1, len(points)):
            if points[x][0] > upperBound:
                numShots += 1
                upperBound = points[x][1]
            else:
                if upperBound > points[x][1]:
                    upperBound = points[x][1]
        return numShots