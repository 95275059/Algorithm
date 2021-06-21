"""
242.有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
说明:你可以假设字符串只包含小写字母。
进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
解题思路：哈希表；排序
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        哈希表
            tt 是 ss 的异位词等价于「两个字符串中字符出现的种类和次数均相等」。
            由于字符串只包含26个小写字母，因此我们可以维护一个长度为26的频次数组table
            先遍历记录字符串s中字符出现的频次，然后遍历字符串t，减去table中对应的频次，如果出现table[i]<0，则说明t包含一个不在s中的额外字符，返回false即可。、
        进阶问题
            核心点在于「字符是离散未知的」，因此我们用哈希表维护对应字符的频次即可。
            同时读者需要注意Unicode一个字符可能对应多个字节的问题，不同语言对于字符串读取处理的方式是不同的。
        时间击败93.90%，内存击败97.07%
        """
        if len(s) != len(t):
            return False
        table = {}
        for i in s:
            table[i] = table[i]+1 if i in table else 1
        for i in t:
            if i not in table:
                return False
            else:
                table[i] -= 1
                if table[i]<0:
                    return False
        return True

    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        排序
            t 是 ss 的异位词等价于「两个字符串排序后相等」。
            因此我们可以对字符串s和t分别排序，看排序后的字符串是否相等即可判断。
            此外，如果s和t的长度不同，t必然不是s的异位词。
        时间击败68.94%，内存击败49.60%
        """
        if len(s) != len(t):
            return False
        s_li = list(s)
        s_li.sort()
        t_li = list(t)
        t_li.sort()
        return True if t_li == s_li else False

if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    #s = "rat"
    #t = "car"
    result = solution.isAnagram1(s, t)
    print(result)
