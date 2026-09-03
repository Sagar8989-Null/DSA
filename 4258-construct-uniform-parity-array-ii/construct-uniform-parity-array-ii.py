class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        
        Min = min(nums1)

        if Min %2 == 1:
            return True 
        else:
            for i in nums1:
                if i % 2 == 1:
                    return False

        return True 