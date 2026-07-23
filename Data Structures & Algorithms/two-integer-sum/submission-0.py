class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            want = target - n
            if want in seen:
                return [seen[want], i]
            seen[n] = i
        raise Exception("no pair found")