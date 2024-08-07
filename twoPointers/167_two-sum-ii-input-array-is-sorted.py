from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        
        while sum != target:
            if sum < target:
                left += 1
            else:
                right -= 1
            sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]