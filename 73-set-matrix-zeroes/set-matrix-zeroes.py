class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def setrowzero(i):
            for j in range(m):
                matrix[i][j] = 0

        def setcolumnzero(j):
            for i in range(n):
                matrix[i][j] = 0

        m = len(matrix[0])
        n = len(matrix)

        hashmap = []

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    hashmap.append([i,j])
                    
        for index in hashmap: 
                setrowzero(index[0])
                setcolumnzero(index[1])