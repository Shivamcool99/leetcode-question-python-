class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim leading and trailing whitespace
        s = s.strip()
        
        length = 0
        i = len(s) - 1
        
        # Iterate backwards to find the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length

        