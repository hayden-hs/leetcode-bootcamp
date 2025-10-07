class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # Initialize result array with 1s
        pref = 1           # Running prefix product
        post = 1           # Running suffix product
        
        # First pass: store prefix products (product of all elements before i)
        for i in range(n):
            answer[i] = pref
            pref *= nums[i]
        
        # Second pass: multiply by suffix products (product of all elements after i)
        for i in range(n - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        
        return answer