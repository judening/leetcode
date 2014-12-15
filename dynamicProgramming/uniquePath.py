class Solution:

    def uniquePaths(self,m,n):
        dp = [[None for i in range(n)] for j in range(m)]
        dp[0][0] = 0
        for i in range(1,n):
            dp[0][i] = 1
        for j in range(1,m):
            dp[j][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        #Be really careful for the corner case
        if m == 1 and n == 1:
            return 1
        return dp[m-1][n-1]