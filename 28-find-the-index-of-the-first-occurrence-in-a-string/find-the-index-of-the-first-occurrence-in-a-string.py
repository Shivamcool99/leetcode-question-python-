class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        # Iterate through haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check substring of haystack starting from i with length equal to needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If no match found, return -1
        return -1