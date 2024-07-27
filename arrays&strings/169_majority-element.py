from typing import List

class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # Revised solution
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
    
    # Initial solution
    # def majorityElement(self, nums: List[int]) -> int:
    #     key = len(nums) // 2
    #     cnt_map = {}
    #     for x in nums:
    #         if x in cnt_map:
    #             cnt_map[x] += 1
    #         else:
    #             cnt_map[x] = 1
    #         if cnt_map[x] > key:
    #             return x
