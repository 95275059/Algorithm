"""
28.实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
测试用例：
haystack = "hello", needle = "ll" : 2;
haystack = "aaaaa", needle = "bba" : -1;
说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
解题思路：双指针，字符串截取；find;index;
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        else:
            len_n = len(needle)
            i = 0
            while i <= len(haystack) - len_n:
                if haystack[i:i + len_n] == needle:
                    return i
                else:
                    i += 1
            return -1

    def strStr1(self, haystack, needle):
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        else:
            return haystack.find(needle)

    def strStr2(self, haystack, needle):
        if needle == '':
            return 0
        elif haystack == '':
            return -1
        else:
            try:
                return haystack.index(needle)
            except:
                return -1

if __name__ == '__main__':
    solution = Solution()
    haystack = 'hello'
    needle = 'll'
    haystack = 'aaaaa'
    needle = 'bba'
    haystack = ''
    needle = '1'
    haystack = 'a'
    needle = ''
    print(solution.strStr(haystack, needle))