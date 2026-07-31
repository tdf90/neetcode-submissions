class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0
        while right > left:
            # record water for left + right & max
            # shift the smaller of the heights inward
            # if this is a new max, record it.
            # since we know that height of water is min(left, right)*(index differece), we know that the taller
            # side is optimized, and the other side can (maybe) be improved. Shifting
            # the taller side wont increase (or match) the max, so we know that wasn't a combination we needed to check
            
            width = right - left
            height = min(heights[left], heights[right])
            water = width * height
            max_water = max(max_water, water)

            # if left is smaller, shift it in
            if heights[left] <= heights[right]:
                left += 1

            else:
                right -= 1

        return max_water
