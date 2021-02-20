class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        # Create cleaned version   
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        
        # Check if palindrome (left right pointer and move inwards)
        left = 0
        right = len(res) - 1
        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True

        
# Test
example = Solution()
print(example.isPalindrome("nitin"))
