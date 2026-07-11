class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        # A - 65
        # Z - 90
        
        ans = 0
        Pow = 0

        columnTitle = columnTitle[::-1]
        
        for i in columnTitle:
            ans = ans + (ord(i) - 64) * 26**Pow
            Pow +=1

        return ans 
