def hr_memo(n,nums,dp):
    if n < 0:
        return 0
    
    if dp[n] != -1:
        return dp[n]
    
    pick = nums[n] + hr_memo(n-2,nums,dp)
    not_pick = hr_memo(n-1,nums,dp)

    dp[n] = max(pick,not_pick)
    return dp[n]

nums = [2, 7, 9, 3, 1]
n = len(nums) - 1
dp = [-1] * (n+1)
print(hr_memo(n,nums,dp))