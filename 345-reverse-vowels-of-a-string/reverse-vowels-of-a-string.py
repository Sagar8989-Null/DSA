class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = {'A','a','E','e','I','i','O','o','U','u'}
        stack = []
        
        res = []

        for i in s:
            if i in vowels: 
                stack.append(i)
                res.append('_')
            else:
                res.append(i)

        for i in range(len(res)):
            if res[i] == '_':
                res[i] = stack.pop()

        return ''.join(res)


            

        
