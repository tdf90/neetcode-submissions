class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            val = numbers[left] + numbers[right]
            if val == target:
                return [1+left, 1+right]
            if val > target:
                right -= 1
                continue
            if val < target:
                left += 1
                continue
        
        return None