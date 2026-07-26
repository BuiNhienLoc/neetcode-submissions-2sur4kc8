class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char not in pairs:            # it's an opening bracket
                stack.append(char)
            else:                            # it's a closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack