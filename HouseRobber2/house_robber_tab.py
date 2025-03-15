def house_robber_tab(nums, start, end):
    if start > end:
        return 0
    dp = [-1] * (len(nums)+1)
    
    dp[0] = nums[start]
    dp[1] = max(nums[0],nums[1])
    
    for i in range(start,end+1):
        pick = nums[i]
        if i > 1:
            pick = nums[i] + dp[i-2]
        not_pick = dp[i-1]
        dp[i] = max(pick, not_pick)
    return dp[end]

def house_robber(nums):
    n = len(nums) 
    if n == 1:
        return nums[0]

    return max(house_robber_tab(nums, 0, n-2), house_robber_tab(nums, 1, n-1))

nums = [2, 3, 2, 5]
print(house_robber(nums))