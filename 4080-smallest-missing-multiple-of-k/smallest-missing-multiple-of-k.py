class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = set(nums)

        i = k
        while i in nums:
            i += k

        return i

            