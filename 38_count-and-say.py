"""
38.外观数列
给定一个正整数 n ，输出外观数列的第 n 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

要 描述 一个数字字符串，首先要将字符串分割为 最小 数量的组，每个组都由连续的最多 相同字符 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。
解题思路：递归，迭代，暴力
"""

class Solution(object):
    def count(self, num_str):
        s = ''
        key = num_str[0:1]
        value = 0
        for i in range(0, len(num_str)):
            if num_str[i] == key:
                value += 1
            else:
                s += (str(value) + key)
                key = num_str[i]
                value = 1
        s += (str(value) + key)
        return s

    def countAndSay(self, n):
        """
        执行用时：20 ms, 在所有 Python 提交中击败了98.77%的用户
        内存消耗：13.1 MB, 在所有 Python 提交中击败了60.39%的用户
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            result = '1'
            for i in range(0, n - 1):
                result = self.count(result)
            return result

    def countAndSay1(self, n):
        """
        递归方法
        递归方法不可避免的会耗时
        执行用时：40 ms, 在所有 Python 提交中击败了29.79%的用户
        内存消耗：13 MB, 在所有 Python 提交中击败了70.93%的用户
        :param n:
        :return:
        """
        if n == 1:
            return "1"
        elif n > 1:
            s = self.countAndSay1(n - 1)
            t = ""
            i, j = 0, len(s)
            count = 1
            while i < j - 1:
                if s[i] == s[i + 1]:
                    count += 1
                else:
                    t = t + str(count) + s[i]
                    count = 1
                i += 1
            t = t + str(count) + s[i]
            return t

    def countAndSay2(self, n):
        """
        递归方法
        同样消耗了过多内存
        执行用时：40 ms, 在所有 Python3 提交中击败了29.79%的用户
        内存消耗：12.9 MB, 在所有 Python3 提交中击败了93.96%的用户
        :param n:
        :return:
        """
        s = "1"
        for i in range(n - 1):
            t = ""
            i, j, count = 0, len(s), 1
            while i < j-1:
                if s[i] == s[i+1]:
                    count += 1
                else:
                    t = t + str(count) + s[i]
                    count = 1
                i += 1
            s = t + str(count) + s[i]
        return s


if __name__ == '__main__':
    n = 5
    solution = Solution()
    print(solution.countAndSay(n))