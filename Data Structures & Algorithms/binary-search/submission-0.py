class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(nums, target, l, h):
            if l > h:
                return -1

            m = l + (h - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                return search(nums, target, l, m - 1)
            else:
                return search(nums, target, m + 1, h)

        return search(nums, target, 0, len(nums) - 1)