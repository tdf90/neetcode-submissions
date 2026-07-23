import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        
        heap = [(-count, n) for n, count in counts.items()]
        heapq.heapify(heap)
        
        out = []
        for _ in range(k):
            _, n = heapq.heappop(heap)
            out.append(n)

        return out

        