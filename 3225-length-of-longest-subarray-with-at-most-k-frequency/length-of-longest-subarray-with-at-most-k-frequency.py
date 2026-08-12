class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            x = nums[right]
            freq[x] = freq.get(x, 0) + 1

            while freq[x] > k:
                freq[nums[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans