class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = {'A','a','E','e','I','i','O','o','U','u'}
        
        res = list(s)

        p1 = 0
        p2 = len(s)-1

        while p1 < p2:
            while p1 < p2 and res[p1] not in vowels:
                p1 += 1

            while p1 < p2 and res[p2] not in vowels:
                p2 -= 1

            res[p1], res[p2] = res[p2], res[p1]

            p1 += 1
            p2 -= 1

            
        return ''.join(res)
            

        
