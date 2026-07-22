class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        reverse_x = int(str(abs(x))[::-1]) * sign
        if reverse_x < -2**31 or reverse_x > 2**31 - 1:
            return 0
        return reverse_x