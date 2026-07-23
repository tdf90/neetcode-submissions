class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = [1] * length
        prefix = suffix = 1

        # Store the product of everything left of i.
        for i, n in enumerate(nums):
            out[i] = prefix
            prefix *= n

        # Multiply by the product of everything right of i.
        for i in reversed(range(length)):
            out[i] *= suffix
            suffix *= nums[i]

        return out