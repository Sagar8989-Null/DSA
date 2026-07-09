class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        res = [-1] * n 
        stack = []
        
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                val = stack.pop()
                res[val] = nums[i % n]
            
            if i < n:
                stack.append(i)

        return res