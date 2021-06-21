"""
7.整数翻转
给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

测试用例：
123 : 321;
-123 : -321;
120 : 21;
0 : 0;
1534236469 : 0;

解题思路：列表反转
"""
class Solution(object):
    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        """
        tmp = int((str(x) if x > 0 else str(-x) + "-")[::-1])
        return tmp if -2 ** 31 < tmp < 2 ** 31 - 1 else 0

    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10
            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        return rev

solution = Solution()
print(solution.reverse(-123))