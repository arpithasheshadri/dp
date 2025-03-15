def house_robber_tab(nums, start, end):
    if start == end:
            return nums[start]
        
    prev2 = nums[start]
    prev1 = max(nums[start], nums[start + 1]) if start + 1 <= end else nums[start]

    for i in range(start+2,end+1):
        curr = max(nums[i] + prev2, prev1)
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