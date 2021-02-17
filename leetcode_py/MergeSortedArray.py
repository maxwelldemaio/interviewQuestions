from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1               # nums1 ptr
        b = n - 1               # nums2 ptr

        for c in range(len(nums1) - 1, -1, -1):
            if b < 0:
                break
            
            # Keep in mind python negative slices go from back of array
            if nums1[a] > nums2[b] and a >= 0:
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1

# Tests
test = Solution()
# print(test.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(test.merge(nums1=[2, 0], m=1, nums2=[1], n=1))



