class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        regis = []
        
        for i in accounts:
            regis.append(sum(i))

        return max(regis)