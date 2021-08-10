"""
8.字符串转换整数（atoi）
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：
    读入字符串并丢弃无用的前导空格
    检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
    读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
    将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
    如果整数数超过 32 位有符号整数范围 [−2^31, 2^31− 1] ，需要截断这个整数，使其保持在这个范围内。
        具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31− 1 的整数应该被固定为 2^31− 1 。
返回整数作为最终结果。
"""
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        时间击败66.28%，内存击败35.18%
        """
        s = s.strip()
        if not len(s):
            return 0
        k = 1 if s[0] in ['+', '-'] else 0
        while k < len(s) and (s[k].isdigit()):
            k += 1
        if k == 1 and s[0] in ['+', '-']:
            return 0
        num = int(s[0:k]) if k>0 else 0
        if num < -2**31:
            return -2**31
        elif num > 2**31-1:
            return 2**31-1
        else:
            return

    def myAtoi1(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        确定有限状态机（deterministic finite automaton, DFA）
        字符串处理的题目往往涉及复杂的流程以及条件情况，如果直接上手写程序，一不小心就会写出极其臃肿的代码。
        因此，为了有条理地分析每个输入字符的处理方法，我们可以使用自动机这个概念：
            我们的程序在每个时刻有一个状态 s，
            每次从序列中输入一个字符 c，并根据字符 c 转移到下一个状态 s'。
            这样，我们只需要建立一个覆盖所有情况的从 s 与 c 映射到 s' 的表格即可解决题目中的问题。
        时间击败7.22%，内存击败59.98%
        """
        automation = Automation()
        for c in s:
            automation.get(c)
        return automation.sign * automation.ans

class Automation:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c: str):
        if c.isspace():
            return 0
        if c=='+' or c=='-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c: str):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans*10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

if __name__ == '__main__':
    solution = Solution()
    s = "+42"
    s = "   -42"
    s = "4193 with words"
    s = "words and 987"
    s = "-91283472332"
    s = "-+12"
    s = "21474836460"
    result = solution.myAtoi1(s)
    print(result)
    print(type(result))