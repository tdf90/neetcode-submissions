import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # entries are unbounded, but frequencies are bounded, 
        # use that as lookup.
        counts = Counter(nums)

        # frequency must be between 0 and len(nums), so we need len(nums) + 1
        # length so frequency[len(nums)] is valid.
        # Use an array so we keep the ordered
        frequency_buckets = [[] for _ in range(len(nums) + 1)]
        for n, count in counts.items():
            frequency_buckets[count].append(n)

        out = []
        for nums in reversed(frequency_buckets):
            for n in nums:
                if len(out) < k:
                    out.append(n)

        return out

        # Solution 2:
        # counts = Counter(nums)
        
        # heap = [(-count, n) for n, count in counts.items()]
        # heapq.heapify(heap)
        
        # out = []
        # for _ in range(k):
        #     _, n = heapq.heappop(heap)
        #     out.append(n)

        # return out

        