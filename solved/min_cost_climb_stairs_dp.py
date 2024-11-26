class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        # bottom up - tabulation
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2,n+1):
            dp[i] = min(dp[i-2] + cost[i-2] , dp[i-1] + cost[i-1])
        
        return dp[n]

        
        