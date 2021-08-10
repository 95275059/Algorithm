"""
118.杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        时间击败94.83%，内存击败66.31%
        """
        result = list()
        for i in range(0, numRows):
            newline = list()
            for j in range(0, i + 1):
                newline.append(1 if j == 0 or j == i else result[i - 1][j - 1] + result[i - 1][j])
            result.append(newline)
        return result


if __name__ == "__main__":
    solution = Solution()
    numRows = 5
    print(solution.generate(numRows))
