from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myDict = {}

        for i in range(len(nums)):
            if nums[i] in myDict:
                return True
            myDict[nums[i]] = 1
        return False


# Example
example = Solution()
print(example.containsDuplicate([1,1,2,3]))
print(example.containsDuplicate([1, 4, 2, 3]))
