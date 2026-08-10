class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "{": "}",
            "(": ")",
            "[": "]",
        }

        for char in s:
            if char in match:
                stack.append(match[char])
                continue

            if not stack or stack.pop() != char:
                return False

        return not stack