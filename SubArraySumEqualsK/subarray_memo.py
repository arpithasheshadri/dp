from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> bool:
        def dfs(index,target):
            if target == 0:
                return True
            if index == 0:
                return nums[index] == target
            not_pick = dfs(index-1,target)
            pick = False
            if k >= nums[index]:
                pick = dfs(index-1, target-nums[index])

            return pick or not_pick
        return dfs(len(nums) - 1, k)
        
sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 5))  # Expected Output: True
print(sol.subarraySum([1, 2, 3], 10))