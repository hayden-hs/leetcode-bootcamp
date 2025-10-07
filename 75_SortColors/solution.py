class Solution(object):
    def sortColors(self, nums):
        i = 0  # Pointer for next position of 0 (left boundary)
        j = len(nums) - 1  # Pointer for next position of 2 (right boundary)
        k = 0  # Current element being examined
        
        while k <= j:
            if nums[k] == 0:  # Found 0: swap to front
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:  # Found 2: swap to end
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
                # Don't increment k: need to check the swapped element
            else:  # Found 1: leave in middle
                k += 1