class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        max_len = 0
        
        for n in values:
            if n-1 not in values:
                length = 1
                current = n + 1
                while current in values:
                    length += 1
                    current += 1
                max_len = max(length, max_len)

        return max_len








