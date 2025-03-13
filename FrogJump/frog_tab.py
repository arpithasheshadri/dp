def frog_tab(n,cost):
    if n == 0:
        return 0
    
    dp = [-1] * (n+1)
    dp[0] = 0

    for i in range(1,n+1):
        left = dp[i-1] + abs(cost[i] - cost[i-1])
        right = float('inf')
        if i > 1:
            right = dp[i-2] + abs(cost[i] - cost[i-2])
        dp[i] = min(left,right)

    return dp[n]


cost = [10,20,30,10,50]
n = len(cost) - 1
print(frog_tab(n,cost))
