class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()

        if len(clean) <= 1:
            return True
    
        half_floow = int(len(clean)/2)
        for i, c in enumerate(clean[:]):
            if clean[len(clean)-i-1] != c:
                return False

        return True