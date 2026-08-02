class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        new = []

        for i in matrix:
            new.extend(i)

        new = set(new)

        if target in new:
            return True 
        else:
            return False