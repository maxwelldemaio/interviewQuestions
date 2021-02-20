class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}

        # Create map from first string
        for char in s:
            if char in sHash:
                sHash[char] += 1
            else:
                sHash[char] = 1

        # Compare for same frequency
        for char in t:
            if char in sHash:
                if sHash[char] < 1:
                    return false
                sHash[char] -= 1
            else:
                return false
