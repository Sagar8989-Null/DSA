class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = 0
        last = [-1, -1, -1]

        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
            count += min(last) + 1

        return count