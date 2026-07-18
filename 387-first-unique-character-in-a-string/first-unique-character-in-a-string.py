class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        Map = {}
    
        for i in s:
            if i not in Map:
                Map[i] = 1
            else:
                Map[i] += 1
        
        for i in range(len(s)):
            if Map[s[i]] == 1:
                return i

        return -1 