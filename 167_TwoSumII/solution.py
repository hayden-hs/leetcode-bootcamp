class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0  # Left pointer (smaller value)
        r = len(numbers) - 1  # Right pointer (larger value)
        
        while l < r:
            sum = numbers[l] + numbers[r]
            
            if sum == target:
                return [l + 1, r + 1]  # Return 1-indexed positions
            elif sum < target:
                l += 1  # Sum too small, move left pointer right
            else:
                r -= 1  # Sum too large, move right pointer left
        
        return []  # No solution found (problem guarantees a solution exists)