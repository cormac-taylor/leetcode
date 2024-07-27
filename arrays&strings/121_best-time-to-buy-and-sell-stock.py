from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        maxDelta = 0
        minPrice = prices[0]
        for x in range(1, len(prices)):
            if prices[x] < minPrice:
                minPrice = prices[x]
            if maxDelta < prices[x] - minPrice:
                maxDelta = prices[x] - minPrice
        return maxDelta