class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}
        for char in s:
            # Add characters to hashmap
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        print(charMap)
        
        # Check if count is 1
        for x in range(len(s)):
            if charMap[s[x]] == 1:
                return x
        return -1

# Tests
example  = Solution()
print(example.firstUniqChar("loveleetcode"))
