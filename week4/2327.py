class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        sharing = 0
        
        for i in range(2, n + 1):
            
            if i - delay > 0:
                sharing = (sharing + dp[i - delay]) % MOD
            
            if i - forget > 0:
                sharing = (sharing - dp[i - forget] + MOD) % MOD
            
            dp[i] = sharing

        total_known = 0
        for i in range(n - forget + 1, n + 1):
            total_known = (total_known + dp[i]) % MOD
            
        return total_known