
class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeros = 0
        Max = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            Max = max(Max, right - left + 1)

        return Max
