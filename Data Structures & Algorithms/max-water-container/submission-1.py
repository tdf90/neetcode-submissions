class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            limiting_height = min(heights[left], heights[right])
            max_area = max(max_area, width * limiting_height)

            # Width will shrink, so only replacing the shorter side
            # could possibly increase the area.
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area