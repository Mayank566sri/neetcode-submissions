class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = set(numbers)
        for i in numbers:
            if target - i in nums:
                return [numbers.index(i)+1, numbers.index(target - i)+1]