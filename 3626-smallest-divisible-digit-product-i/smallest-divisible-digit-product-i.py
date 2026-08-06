class Solution(object):

    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        
        def product(no):
            if no < 10:
                return no
            else:
                unit = no%10
                tens = int(no/10)
                return unit * tens

        for i in range(n,101):
            if product(i) % t == 0:
                return i


        
        