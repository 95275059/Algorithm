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

solution = Solution()
print(solution.reverse(-123))