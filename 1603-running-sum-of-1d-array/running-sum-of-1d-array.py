class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total = 0 
        res = []
        for i in nums:
            total += i 
            res.append(total)

        return res