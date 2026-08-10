class Solution:

    want = {}

    def isValid(self, s: str) -> bool:
        stack = []
        match = {"{":"}", "(":")", "[":"]"}
        for c in s:
            if c in match:
                stack.append(match[c])
                continue
            if c in {"}", "]", ")"}:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if c != last:
                    return False

        return len(stack) == 0
