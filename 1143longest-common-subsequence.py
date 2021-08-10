"""
1143.最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：
    它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
    例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
解题思路：动态规划
    最长公共子序列问题是典型的二维动态规划问题。
    假设字符串 text1 和 text2 的长度分别为 m 和 n，创建 m+1 行 n+1 列的二维数组 dp，
    其中 dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列的长度。
    上述表示中，text1[0:i] 表示 text1的长度为 i 的前缀，text2[0:j] 表示 text2的长度为 j 的前缀。
    考虑动态规划的边界情况：
        当 i=0 时，text1[0:i] 为空，空字符串和任何字符串的最长公共子序列的长度都是 0，因此对任意 0≤j≤n，有 dp[0][j]=0；
        当 j=0 时，text2[0:j] 为空，同理可得，对任意 0≤i≤m，有 dp[i][0]=0。
        因此动态规划的边界情况是：当 i=0 或 j=0 时，dp[i][j]=0。
    当 i>0i>0 且 j>0j>0 时，dp[i][j] 的计算：
        当 text1[i−1]=text2[j−1] 时，将这两个相同的字符称为公共字符，
            考虑 text1[0:i−1] 和 text2[0:j−1] 的最长公共子序列，再增加一个字符（即公共字符）即可得到 text1[0:i] 和 text2[0:j] 的最长公共子序列
            因此 dp[i][j]=dp[i−1][j−1]+1。
        当 text1[i−1]!=text2[j−1] 时，考虑以下两项：text1[0:i−1] 和 text2[0:j] 的最长公共子序列；text1[0:i] 和 text2[0:j−1] 的最长公共子序列。
            要得到 text1[0:i] 和 text2[0:j] 的最长公共子序列，应取两项中的长度较大的一项，
            因此 dp[i][j]=max(dp[i−1][j],dp[i][j−1])。
    由此可以得到如下状态转移方程
    最终计算得到 dp[m][n] 即为 text1和 text2的最长公共子序列的长度。
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        时间击败98.02%，内存击败95.71%
        """
        len1, len2 = len(text1), len(text2)
        f = [[0] *(len2+1) for _ in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if text1[i-1] == text2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    f[i][j] = max(f[i-1][j], f[i][j-1])
        return f[len1][len2]