class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0 
        right = len(height) -1
        LeftMAX = 0
        RightMAX = 0
        count = 0

        while left <= right:

            if height[left] <= height[right]:
                LeftMAX = max(LeftMAX, height[left])
                count += LeftMAX - height[left]
                left += 1

            else:
                RightMAX = max(RightMAX, height[right])
                count += RightMAX - height[right]
                right -= 1

        return count
        
