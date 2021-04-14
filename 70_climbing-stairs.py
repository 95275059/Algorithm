"""
70.爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
解题思路：动态规划，可以通过递归和迭代的方式实现
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        超出时间限制2333，从后往前看
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs1(self, n):
        """
        从前往后看
        """
        if n <= 2:
            return n
        point1 = 1
        point2 = 2
        for i in range(3, n+1):
            temp = point1 + point2
            point1 = point2
            point2 = temp
        return point2


if __name__ == '__main__':
 solution = Solution()
 num = 38
 print(solution.climbStairs(num))