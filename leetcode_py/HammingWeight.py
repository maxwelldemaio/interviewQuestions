class Solution:
    def hammingWeight(self, n: int) -> int:
        weight = 0
        while n > 0:
            weight += n & 1
            # Shift bits to the right until we reach the end
            n >>= 1
        return weight

# Tests
example = Solution()
print(example.hammingWeight(3))
