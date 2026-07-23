class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        out = [1] * length
        prefix = suffix = 1

        # prefix[i] is product of items to left
        for i, n in enumerate(nums):
            out[i] = prefix
            prefix *= n

        # suffix[i] is product of items to right
        # multiply by existing prefix[i] to get 
        # output
        for i in reversed(range(length)):
            out[i] *= suffix
            suffix *= nums[i]

        return out
