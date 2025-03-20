class Solution:
    def lcs_recursive(self,i,j,text1,text2,dp):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if text1[i] == text2[j]:
            dp[i][j] = 1 + self.lcs_recursive(i-1,j-1,text1,text2,dp)
        else:
            dp[i][j] = max(self.lcs_recursive(i-1,j,text1,text2,dp), self.lcs_recursive(i,j-1,text1,text2,dp))
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        return self.lcs_recursive(m-1,n-1,text1,text2,dp)
    
sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace"))
    
