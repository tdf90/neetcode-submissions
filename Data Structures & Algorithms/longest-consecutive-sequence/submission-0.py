class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequences_starts = set()
        all_vals = set()
        for n in nums:
            sequences_starts.add(n)
            all_vals.add(n)
        for n in nums:
            if n-1 in sequences_starts:
                sequences_starts.discard(n)
        
        max_len = 0
        for start in sequences_starts:
            length = 1
            next = start + 1
            while next in nums:
                length += 1
                next += 1
            if length > max_len:
                max_len = length

        return max_len








