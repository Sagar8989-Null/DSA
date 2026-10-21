class Solution(object):
    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        m = len(mat[0])
        n = len(mat)
        Max = 0 
        coor = [0,0]

        for i in range(n):
            for j in range(m):
                if Max < mat[i][j]:
                    Max = mat[i][j]
                    coor[0]= i
                    coor[1]= j


        return coor