"""
14.最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

测试用例：
strs = ["flower","flow","flight"] : "fl";
strs = ["dog","racecar","car"] : "" ; 输入不存在公共前缀。

提示：
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

解题思路：水平扫描法;利用python的max()和min();利用python的zip函数;
https://www.jianshu.com/p/4ef3cfa01367
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        result = strs[0]
        strs.pop(0)
        for s in strs:
            new_result = ''
            length = len(s) if len(s) < len(result) else len(result)
            for i in range(0, length):
                if s[i:i+1] == result[i:i+1]:
                    new_result += s[i:i+1]
                else:
                    break
            result = new_result
            if result == '':
                break
        return result

    # 用python的max()和min(), 在Python里字符串是可以比较的，按照ascII值排，
    # 举例abb， aba，abac，最大为abb，最小为aba。
    # 所以只需要比较最大最小的公共前缀就是整个数组的公共前缀
    def longestCommonPrefix1(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    # 利用python的zip函数，把str看成list然后把输入看成二维数组
    # 左对齐纵向压缩，然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
    def longestCommonPrefix2(self, strs):
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        print(ss)
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            print(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

solution = Solution()
print(solution.longestCommonPrefix2(["flower","flow","flight"]))
