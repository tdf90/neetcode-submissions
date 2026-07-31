class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        active_chars = set()

        for right, char in enumerate(s):
            while char in active_chars:
                active_chars.remove(s[left])
                left += 1

            active_chars.add(char)
            longest = max(longest, right - left + 1)

        return longest