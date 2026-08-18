class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        n = len(nums)
        freq = {}

        for j in range(n - k + 1):
            seen = set()

            for i in range(j, j + k):
                seen.add(nums[i])

            for num in seen:
                freq[num] = freq.get(num, 0) + 1

        ans = -1

        for num, count in freq.items():
            if count == 1:
                ans = max(ans, num)

        return ans