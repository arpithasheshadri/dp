def house_robber_tab(nums, start, end):
    if start > end:
            return 0
    n = end-start+1
    dp = [-1] * (n)
    dp[0] = nums[start]
    if n > 1:
        dp[1] = max(nums[start], nums[start+1])

    for i in range(2,n):
        dp[i] = max(nums[start+i] + dp[i-2], dp[i-1])
    return dp[-1]


def house_robber(nums):
    n = len(nums) 
    if n == 1:
        return nums[0]

    return max(house_robber_tab(nums, 0, n-2), house_robber_tab(nums, 1, n-1))

nums = [2, 3, 2, 5]
print(house_robber(nums))