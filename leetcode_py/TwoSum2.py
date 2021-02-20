from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for x in range(len(nums)):
            # Check if match
            if nums[x] in myHash:
                return [x, myHash[nums[x]]]
            else:
                myHash[target - nums[x]] = x

        # Tests
example = Solution()
print(example.twoSum(nums=[2,7,11,15], target=9))
