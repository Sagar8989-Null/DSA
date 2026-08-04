class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = max(nums)
        m = min(nums)
        nums = set(nums)
        res = []

        for i in range(m,n):
            if i not in nums:
                res.append(i) 

        return res
