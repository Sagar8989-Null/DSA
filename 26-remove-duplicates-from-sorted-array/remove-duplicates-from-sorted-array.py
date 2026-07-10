class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        i = 0 
        for j in range(1,n):

            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1

        return i+1
