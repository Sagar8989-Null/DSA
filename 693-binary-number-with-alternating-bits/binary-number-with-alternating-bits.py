class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        n = bin(n)
        l = len(n)

        for i in range(1,len(n)):
            if n[i-1] == n[i]:
                return False

        return True            