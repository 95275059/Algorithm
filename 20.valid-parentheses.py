"""
20.有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合
测试用例：
s = "()"  : True;
s = "()[]{}" : True;
s = "(]" : False;
s = "([)]" : False;
s = "{[]}" : True;
解题思路：堆栈
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return s == ''

    def isValid1(self, s):
        stack = []
        map = {'(': ')', '[': ']', '{': '}'}
        for i in range(0, len(s)):
            if s[i] in map.keys():
                stack.append(s[i])
            for key, value in map.items():
                if s[i] == value:
                    if stack and stack[-1] == key:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0

    def isValid2(self, s):
        stack = []
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return len(stack) == 0

solution = Solution()
print(solution.isValid("()[]{}"))