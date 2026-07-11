class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def PAS(List):
            s = [1]
            for i in range(1,len(List)):
                s.append(List[i-1]+List[i])

            s.append(1)
            return s

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
    

        res = [[1],[1,1]]
        numRows = numRows - 2

        while numRows:
            res.append(PAS(res[-1]))
            numRows -= 1

        return res
        

