from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [[False] * (k+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        for i in range(n):
            for target in range(k+1):
                not_pick = dp[i-1][target]
                pick = False
                if target >= nums[i]:
                    pick = dp[i-1][target-nums[i]]
                dp[i][target] = pick or not_pick

            
        return dp[n-1][k]
        
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 5))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 10))