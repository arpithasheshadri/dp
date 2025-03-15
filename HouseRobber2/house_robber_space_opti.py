def house_robber_tab(nums, start, end):
    if start > end:
        return 0
    
    
    prev1 = nums[start]
    prev2 = 0
    
    for i in range(start,end+1):
        pick = nums[i]
        if i > 1:
            pick = nums[i] + prev2
        not_pick = prev1
        curr = max(pick, not_pick)
        prev2 = prev1
        prev1 = curr
    return prev1

def house_robber(nums):
    n = len(nums) 
    if n == 1:
        return nums[0]

    return max(house_robber_tab(nums, 0, n-2), house_robber_tab(nums, 1, n-1))

nums = [2, 3, 2, 5]
print(house_robber(nums))