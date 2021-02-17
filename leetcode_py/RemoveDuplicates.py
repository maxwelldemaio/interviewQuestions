from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # (j) last index to overwrite on
        # (i) iterator
        j = 1

        for i in range(1, len(nums)):
            # Unique number found
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        
# Test
example = Solution()
# Return length of non-duplicate array
# Array should have sorted elements at beginning
print(example.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
