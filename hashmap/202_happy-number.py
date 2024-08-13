class Solution:
    """
    Time complexity: O(log(n))
    Space complexity: O(log(n))
    """
    def isHappy(self, n: int) -> bool:
        seenNums = set()
        sum = 0
        num = n
        while num != 1 and num not in seenNums:
            seenNums.add(num)
            while num != 0:
                digit = num % 10
                sum += digit * digit
                num //= 10
            num = sum
            sum = 0
        return num == 1
