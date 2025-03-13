def fib_memo(n,dp):
    if n <= 1:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] =fib_memo(n-1,dp) + fib_memo(n-2,dp)
    return dp[n]

n = 10
dp = [-1] * (n+1)
print(fib_memo(n,dp))