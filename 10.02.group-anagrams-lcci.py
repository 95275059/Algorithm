"""
面试题10.02.变位词组
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
注意：本题相对原题稍作修改
说明：所有输入均为小写字母。不考虑答案输出的顺序。
测试用例：
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
    输出:[["ate","eat","tea"], ["nat","tan"], ["bat"]]
解题思路：排序；计数
"""
import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        时间击败8.57%，内存击败8.57%
        """
        set_map, result = list(), list()
        for str in strs:
            ss = list(str)
            ss.sort()
            flag = False
            for i, value in enumerate(set_map):
                if value == ss:
                    result[i].append(str)
                    flag = True
                    break
            if not flag:
                set_map.append(ss)
                result.append([str])
        print(set_map)
        print(result)
        return result

    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        排序
        由于互为变位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的键。
        时间击败100.00%，内存击败54.29%
        """
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        计数
        由于互为变位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。
        由于字符串只包含小写字母，因此对于每个字符串，可以使用长度为 26 的数组记录每个字母出现的次数。
        需要注意的是，在使用数组作为哈希表的键时，不同语言的支持程度不同，因此不同语言的实现方式也不同。
        时间击败85.71%，内存击败5.72%
        """
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        return list(mp.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))