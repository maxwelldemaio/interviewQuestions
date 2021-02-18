from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        # Swap spots
        # have to use nums[:] and not nums
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


# Tests
example = Solution()
print(example.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
