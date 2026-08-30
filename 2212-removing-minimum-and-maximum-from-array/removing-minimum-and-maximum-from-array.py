class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        Max_i = nums.index(max(nums))
        Min_i = nums.index(min(nums))

        left = min(Max_i, Min_i)
        right = max(Max_i, Min_i)

        option1 = right + 1

        option2 = n - left

        option3 = (left + 1) + (n - right)

        return min(option1, option2, option3)