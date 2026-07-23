import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        heap = []
        for n, count in freqs.items():
            heapq.heappush(heap, (-count, n))
        
        out = []
        for _ in range(k):
            neg_count, n = heapq.heappop(heap)
            out.append(n)

        return out

        