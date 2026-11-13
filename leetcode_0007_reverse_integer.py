class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x:
            digit = x % 10
            if rev > (INT_MAX - digit) // 10:
                return 0
            rev = rev * 10 + digit
            x //= 10
        return sign * rev

sol = Solution()
print(sol.reverse(0))