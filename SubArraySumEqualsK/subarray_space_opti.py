from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = [False] * (k+1)
        curr = [False] * (k+1)
        prev[0] = True
        curr[0] = True
        prev[nums[0]] = True
        for i in range(n):
            for target in range(k+1):
                not_pick = prev[target]
                pick = False
                if target >= nums[i]:
                    pick = prev[target-nums[i]]
                curr[target] = pick or not_pick
            prev = curr.copy()

            
        return prev[k]
        
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 5))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 10))