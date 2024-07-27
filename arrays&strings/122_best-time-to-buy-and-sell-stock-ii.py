from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        theoMax = 0
        yesterday = prices[0]
        for today in range(1, len(prices)):
            if prices[today] > yesterday:
                theoMax += prices[today] - yesterday
            yesterday = prices[today]
        return theoMax

