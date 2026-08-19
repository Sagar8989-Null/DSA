class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """

        reserved = {}

        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()

            reserved[row].add(seat)

        ans = (n - len(reserved)) * 2

        for seats in reserved.values():

            left = not any(s in seats for s in [2, 3, 4, 5])
            middle = not any(s in seats for s in [4, 5, 6, 7])
            right = not any(s in seats for s in [6, 7, 8, 9])

            if left and right:
                ans += 2

            elif left or middle or right:
                ans += 1

        return ans