def frog_memo(n,cost,dp):
    if n == 0:
        return 0
    
    if n == 1:
        return abs(cost[1] - cost[0])
    
    if dp[n] != -1:
        return dp[n]
    
    left = frog_memo(n-1,cost,dp) + abs(cost[n] - cost[n-1])
    right = float('inf')
    if n > 1:
        right = frog_memo(n-2,cost,dp) + abs(cost[n] - cost[n-2])
    
    dp[n] = min(left,right)
    return dp[n]

cost = [10,20,30,10,50]
n = len(cost) - 1
dp = [-1] * (n+1)
print(frog_memo(n, cost, dp))