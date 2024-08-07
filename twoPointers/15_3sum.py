class Solution(object):
    """
    Time complexity: O(n^2)
    Space complexity: O(n^2), worst case output quadratic [-1,1,-2,2,...,-(n-1),n-1,-n,n]
    """
    # inspired from solutions tab
    def threeSum(self, nums):
        res = set()

        positiveList, negativeList, numZeros = [], [], 0
        for num in nums:
            if num > 0:
                positiveList.append(num)
            elif num < 0: 
                negativeList.append(num)
            else:
                numZeros += 1

        positiveSet, negativeSet = set(positiveList), set(negativeList)

        # cases with 0
        if numZeros > 0:
            for num in positiveSet:
                if -num in negativeSet:
                    res.add((-num, 0, num))
            
            if numZeros >= 3:
                res.add((0,0,0))

        # cases with negative complement
        for i in range(len(positiveList)):
            for j in range(i+1,len(positiveList)):
                complement = -(positiveList[i] + positiveList[j])
                if complement in negativeSet:
                    res.add((complement, \
                             min(positiveList[i], positiveList[j]), \
                             max(positiveList[i], positiveList[j])))

        # cases with positive complement
        for i in range(len(negativeList)):
            for j in range(i+1,len(negativeList)):
                complement = -(negativeList[i] + negativeList[j])
                if complement in positiveSet:
                    res.add((min(negativeList[i], negativeList[j]), \
                             max(negativeList[i], negativeList[j]), \
                             complement))

        return res