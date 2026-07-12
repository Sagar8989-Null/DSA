class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        single = []

        for List in matrix:
            single.extend(List)

        single = set(single)

        return (target in single)
        