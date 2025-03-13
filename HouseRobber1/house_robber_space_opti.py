def hr_memo(n,nums):
    if n < 0:
        return 0
    

    prev1 = nums[0]
    prev2 = 0
    
    for i in range(1,n+1):
        pick = nums[i]
        if i > 1:
            pick = nums[i] + prev2
        not_pick = prev1
        prev2 = prev1
        prev1 = max(pick,not_pick)
    return prev1

    return dp[n]

nums = [2, 7, 9, 3, 1]
n = len(nums) - 1

print(hr_memo(n,nums))