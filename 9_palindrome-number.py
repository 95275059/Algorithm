"""
9.回文数
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

测试用例：
121 : true ;
-121 : false(从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。);
10 : false;
-101 : false;

解题思路：列表反转或正常倒着算
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        old = str(x)
        new = str(x)[::-1]
        return old==new

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        tmp = x
        y = 0
        while tmp>0:
            yu = tmp%10
            y = y*10 + yu
            tmp = int(tmp/10)
        return y == x

solution = Solution()
print(solution.isPalindrome(1))