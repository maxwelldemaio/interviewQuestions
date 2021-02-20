from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            print(digits[i])
            # Increment number and return
            if digits[i] < 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
        # all 9 case
        digits.insert(0, 1)
        return digits

# Tests
example = Solution()
# example.plusOne([9,9,9])
print(example.plusOne([1,2,3]))
# example.plusOne([1,2,9])
