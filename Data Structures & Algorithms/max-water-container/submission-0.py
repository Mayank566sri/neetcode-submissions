class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights)-1
        Max = 0
        while l<h:
            width = h-l
            length = min(heights[l], heights[h])
            area = width * length

            if area > Max:
                Max = area
            if heights[l] < heights[h]:
                l+=1
            else:
                h-=1
        return Max