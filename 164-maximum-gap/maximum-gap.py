class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        MAX = 0 
        if n < 2:
            return 0

        nums.sort()

        for i in range(1,n):
            val = (nums[i]-nums[i-1])
            if MAX < val:
                MAX = val

        return MAX