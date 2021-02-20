from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[anchor]
                nums[anchor] = temp
                anchor += 1
        return nums

# Tests
example = Solution()
print(example.moveZeroes([1,3,9,0,7,0,6]))
