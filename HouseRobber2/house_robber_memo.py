def house_robber_memo(nums, start, end, dp):
    if start > end:
        return 0
    
    if dp[end] != -1:
        return dp[end]
    
    dp[end] = max(nums[end] + house_robber_memo(nums, start, end - 2, dp), house_robber_memo(nums, start, end - 1, dp))
    return dp[end]

def house_robber(nums):
    n = len(nums) 
    if n == 1:
        return nums[0]
    
    dp1 = [-1] * (n+1)
    dp2 = [-1] * (n+1)

    return max(house_robber_memo(nums, 0, n-2, dp1), house_robber_memo(nums, 1, n-1, dp2))

nums = [2, 3, 2, 5]
print(house_robber(nums))