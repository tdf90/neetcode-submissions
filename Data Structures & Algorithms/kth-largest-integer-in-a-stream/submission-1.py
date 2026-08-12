import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        # nums is a min heap, so we can take away
        # the smallest until we just have k left
        # then we know that the top is the kth smallest
        while len(nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)

        # self.nums has k values, now it has k+1
        # pop the last item to discard.
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
