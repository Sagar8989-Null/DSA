class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        for x in nums:
            r = x % 3
            ans += min(r, 3 - r)

        return ans