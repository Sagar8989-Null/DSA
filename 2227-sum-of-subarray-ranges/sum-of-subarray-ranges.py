class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        ans = 0

        for i in range(n):
            Min = Max = nums[i]
            for j in range(i, n):
                Min = min(Min, nums[j])
                Max = max(Max, nums[j])
                ans += Max - Min

        return ans


        