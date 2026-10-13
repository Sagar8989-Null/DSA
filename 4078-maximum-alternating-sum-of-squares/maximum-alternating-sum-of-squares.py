class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort(key=lambda x: x * x)
        n = len(nums)
        half = n // 2

        return sum(x * x for x in nums[half:]) - sum(x * x for x in nums[:half])
