# Leetcode: https://leetcode.com/problems/powx-n/description/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Base case: anything to the power of 0 is 1

        if n < 0:
            x = 1 / x  # Invert x if n is negative
            n = -n

        return self.power(x, n)

    def power(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Base case for recursion

        half = self.power(x, n // 2)

        if n % 2 == 0:
            return half * half  # If n is even
        else:
            return half * half * x  # If n is odd
