def hr_memo(n,nums):
    if n < 0:
        return 0
    dp = [-1] * (n+1)

    dp[0] = nums[0]
    
    for i in range(1,n+1):
        pick = nums[i]
        if i > 1:
            pick = nums[i] + dp[i-2]
        not_pick = nums[i-1]
        dp[i] = max(pick,not_pick)

    return dp[n]

nums = [2, 7, 9, 3, 1]
n = len(nums) - 1

print(hr_memo(n,nums))