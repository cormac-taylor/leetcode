class Solution:
    """
    Time complexity: O(m+n)
    Space complexity: O(1)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # indexes at the end of each array
        indexNums1 = m - 1
        indexNums2 = n - 1
        indexResult = m + n - 1

        # while both not empty move the larger value to the result
        while indexNums1 >= 0 and indexNums2 >= 0:
            if nums1[indexNums1] > nums2[indexNums2]:
                nums1[indexResult] = nums1[indexNums1]
                indexNums1 -= 1
            else:
                nums1[indexResult] = nums2[indexNums2]
                indexNums2 -= 1
            indexResult -= 1

        # move the rest of the values to the result
        if indexNums1 < 0:
            while indexNums2 >= 0:
                nums1[indexResult] = nums2[indexNums2]
                indexNums2 -= 1
                indexResult -= 1
        else:
            while indexNums1 >= 0:
                nums1[indexResult] = nums1[indexNums1]
                indexNums1 -= 1
                indexResult -= 1