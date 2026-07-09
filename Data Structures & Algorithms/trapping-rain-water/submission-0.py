class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        leftmax, rightmax, total = 0,0,0
        while start< end:
            leftmax = max(leftmax, height[start])
            rightmax = max(rightmax, height[end])
            if leftmax < rightmax:
                total += leftmax - height[start]
                start += 1
            else:
                total += rightmax - height[end]
                end -= 1
        return total