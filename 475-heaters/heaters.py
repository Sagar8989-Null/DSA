class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        heaters.sort()
        ans = 0

        for house in houses:
            left, right = 0, len(heaters)

            while left < right:
                mid = (left + right) // 2
                
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid

            i = left

            d1 = house - heaters[i - 1] if i > 0 else float('inf')
            d2 = heaters[i] - house if i < len(heaters) else float('inf')
            ans = max(ans, min(d1, d2))

        return ans

        
