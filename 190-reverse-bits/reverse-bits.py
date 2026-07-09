class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        p = (32-len(n))
        n = ('0'*p) + n 
        n = int(n[::-1],2)

        return n