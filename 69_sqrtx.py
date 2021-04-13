"""
69.x的平方根
计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
解题思路：二分法，牛顿迭代法
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        4468ms 12.8mb
        """
        if x == 1:
            return 1
        i = 1
        while i <= int(x/2):
            if i*i > x:
                break
            i += 1
        return i-1

    def mySqrt1(self, x):
        """
        二分法
        28ms 13mb
        """
        if x == 1:
            return 1
        min = 0
        max = x
        while max - min > 1:
            mid = (max + min) // 2
            if x/mid < mid:
                max = mid
            else:
                min = mid
        return int(min)

    def mySqrt2(self, x):
        """
        牛顿迭代法
        计算平方根，最好和使用最多的方法是牛顿法
        32ms 13MB
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)

if __name__ == '__main__':
    solution = Solution()
    x = 3
    print(solution.mySqrt1(x))