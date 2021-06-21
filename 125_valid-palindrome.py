"""
125.验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
解题思路：双指针,先筛选再判断
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        双指针
        时间击败23.12%，内存击败92.57%
        """
        if not len(s):
            return True
        left, right = 0, len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1
            if left<right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left+1, right-1
        return True

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        先筛选再判断
        筛选出字母和数字，然后就变成直接判断是否为回文字符串的问题
        判断除了使用双指针的方法，可以通过直接翻转字符串然后进行比较进行
        时间击败78.78%，内存击败27.49%
        """
        new_s = "".join(i.lower() for i in s if i.isalnum())
        return new_s == new_s[::-1]