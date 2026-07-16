class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        l, r = 0, len(nums)-1
        m = l + (r-l)//2
        if len(nums)%2 == 0:
            return float((nums[m] + nums[m+1])/2)
        if len(nums)%2 != 0:
            return float(nums[m])