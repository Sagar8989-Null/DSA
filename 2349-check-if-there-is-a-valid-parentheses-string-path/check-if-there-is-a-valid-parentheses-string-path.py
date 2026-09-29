class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """

        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 == 1:
            return False

        dp = [set() for _ in range(n)]

        for i in range(m):
            for j in range(n):
                new_balances = set()

                value = 1 if grid[i][j] == '(' else -1

                if i == 0 and j == 0:
                    if value == 1:
                        new_balances.add(1)
                else:
                    if i > 0:
                        for balance in dp[j]:
                            new_balance = balance + value
                            if new_balance >= 0:
                                new_balances.add(new_balance)

                    if j > 0:
                        for balance in dp[j - 1]:
                            new_balance = balance + value
                            if new_balance >= 0:
                                new_balances.add(new_balance)

                dp[j] = new_balances

        return 0 in dp[n - 1]