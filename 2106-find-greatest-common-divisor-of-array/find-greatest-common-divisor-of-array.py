class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        Max = max(nums)
        Min = min(nums)

        for i in range(Min+1,0,-1):
            if Min % i  == 0 and Max % i == 0:
                return i
            
