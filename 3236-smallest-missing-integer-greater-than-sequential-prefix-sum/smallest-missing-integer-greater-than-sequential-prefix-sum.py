class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        if n < 1:
            return 0

        Sum = nums[0]

        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                Sum += nums[i]
            else:
                break
            
        while True:
            if Sum not in nums:
                return Sum

            Sum += 1
        

