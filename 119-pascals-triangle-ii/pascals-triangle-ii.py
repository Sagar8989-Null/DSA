class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def PAS(List):
            s = [1]
            for i in range(1,len(List)):
                s.append(List[i-1]+List[i])
            s.append(1)

            return s

        res=[[1],[1,1]]

        for i in range(rowIndex-1):
            res.append(PAS(res[-1]))

        return res[rowIndex]

        
        