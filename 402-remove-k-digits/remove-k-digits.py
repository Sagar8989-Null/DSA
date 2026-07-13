class Solution(object):
    def removeKdigits(self, num, k):

        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        n = len(num)
        mono = []

        for i in range(n):
            while mono and k> 0 and num[i] < mono[-1]:
                mono.pop()
                k -= 1

            mono.append(num[i])
        
        while mono and k > 0:
            mono.pop()
            k -= 1

        return ''.join(mono).lstrip('0') or "0"
