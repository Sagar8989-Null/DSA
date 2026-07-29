class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum = 0 
        even = True

        for i in range(len(nums)):
            if even:
                sum += nums[i]
                even = False
            else:
                sum -= nums[i]
                even = True

        return sum