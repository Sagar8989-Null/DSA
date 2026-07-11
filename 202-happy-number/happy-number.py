class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def Next(n):
            Sum = 0 
            while n:
                Sum += (n % 10)**2
                n //=10
            return Sum 
        
        seen = set()

        while n != 1 :

            if n in seen:
                return False

            seen.add(n)
            n = Next(n)

        return True
            