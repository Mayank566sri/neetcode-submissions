class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'{':'}', '[':']', '(':')'}
        stack = []
        for x in s:
            if x in pair:
                stack.append(x)
            elif len(stack) == 0 or pair[stack.pop()] != x:
                return False
        return len(stack) == 0