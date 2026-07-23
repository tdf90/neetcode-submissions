class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        out = [0] * l
        prefix = suffix = 1
        for i, n in enumerate(nums):
            out[i] = prefix
            prefix *= n
        for i in reversed(range(l)):
            out[i] *= suffix
            suffix *= nums[i]
        return out
