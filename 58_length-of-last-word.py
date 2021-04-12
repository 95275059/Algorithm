"""
58.最后一个单词的长度
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
题解：注意最后一个字符是空格的情况，不过split可以自己解决就是了。正常解法是从后往前判断，注意末尾是空格的情况
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_list = s.split()
        if word_list:
            return len(word_list[-1])
        else:
            return 0

    def lengthOfLastWord1(self, s):
        length = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] != ' ':
                length += 1
            elif length:
                return length
            i -= 1
        return length

if __name__ == '__main__':
 solution = Solution()
 s = "Hello World "
 s = "a "
 print(solution.lengthOfLastWord(s))