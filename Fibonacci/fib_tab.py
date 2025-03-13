def fib_tab(n):
    if n <= 1:
        return n
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

n = 10
print(fib_tab(n))