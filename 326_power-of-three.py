"""
326.3的幂
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3^x
进阶：你能不使用循环或者递归来完成本题吗？
解题思路：循环迭代；基准转换
1.循环迭代
找出数字 n 是否是数字 b 的幂的一个简单方法是，n%3 只要余数为 0，就一直将 n 除以 b
因此，应该可以将 n 除以 b x 次，每次都有 0 的余数，最终结果是 1。
2.基准转换
在基数 10 中，10 的所有幂都从数字 1 开始，然后只跟 0（例如10、100、1000）。其他基数和各自的权重也是如此。
因此，如果我们把我们的数转换成基3，并且表示形式是 100…0，那么这个数就是3的幂。
我们所要做的就是将数字转换为以3为底的基数 ，并检查它是否为前导1，后跟所有 0。
两个内置的Java函数将帮助我们前进。
    String baseChange = Integer.toString(number, base);
        上面的代码将 number 转换以 base 为底的基数，并以字符串形式返回结果。
        例如，integer.toString（5，2）=“101” 和 integer.toString（5，3）=“12”。
    boolean matches = myString.matches("123");
        上面的代码检查字符串中是否存在特定的正则表达式。
        例如，如果字符串 mystring 中存在子字符串 “123”，上面的内容将返回 true。
        boolean powerOfThree = baseChange.matches("^10*$")
        我们将使用上面的正则表达式来检查字符串是否以1 ^1 开头，后跟 0 或 多个 0 0* 并且不包含任何其他值 $。
3.运算法
n = 3^i
i = log3(n)
i = logb(n)/logb(3)
"""
import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        循环迭代
        时间击败26.70%，内存击败39.77%
        """
        if n<1:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1

    def isPowerOfThree1(self, n):
        """
        :type n: int
        :rtype: bool
        循环迭代
        时间击败81.53%，内存击败19.03%
        """
        if n < 1:
            return False
        i = round(math.log(n)/math.log(3))
        pow = 3**i
        return pow == n
