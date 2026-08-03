class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        S = set([i for i in s])
        return len(S)