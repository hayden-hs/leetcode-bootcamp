class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_max_crossing_sum(l, m, r):
            
            left_sum = float('-inf')
            curr = 0
            for i in range(m, l - 1, -1):
                curr += nums[i]
                left_sum = max(left_sum, curr)
            
            
            right_sum = float('-inf')
            curr = 0
            for i in range(m + 1, r + 1):
                curr += nums[i]
                right_sum = max(right_sum, curr)
                
            return left_sum + right_sum

        def solve(l, r):
            if l == r:
                return nums[l]
            
            mid = (l + r) // 2
            
            
            return max(solve(l, mid), 
                       solve(mid + 1, r), 
                       find_max_crossing_sum(l, mid, r))

        return solve(0, len(nums) - 1)