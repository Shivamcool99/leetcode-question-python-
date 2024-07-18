class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            elif ch in mapping.keys():
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                return False
        
        return len(stack) == 0