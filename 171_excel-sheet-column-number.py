"""
171.Excel表序列号
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
解题思路：进制转换
"""


class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        时间击败43.65%，内存击败93.49%
        """
        result, multiple =0, 1
        for i in range(len(columnTitle)-1, -1, -1):
            k = ord(columnTitle[i]) - ord('A') + 1
            result += k*multiple
            multiple *= 26
        return result

if __name__ == "__main__":
    solution = Solution()
    columnTitle = 'AB'
    print(solution.titleToNumber(columnTitle))
