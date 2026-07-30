class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i, n in enumerate(nums):
            right = len(nums)-1
            left = i+1
            while right > left:
                if nums[right] + nums[left] == -n:
                    # tuple is already sorted since the nums are.
                    triplets.add((nums[i], nums[left], nums[right]))
                    
                    # see if another pair also sum.
                    left += 1
                    right -= 1
                elif nums[right] + nums[left] >= -n:
                    right -= 1
                else:
                    left += 1

        return [list(tup) for tup in triplets]

        