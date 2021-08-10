"""
1736.替换隐藏数字得到的最晚时间
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。
有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。
替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。
"""


class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        贪心
        时间击败64.86%，内存击败18.92%
        """
        time_li = list(time)
        if time_li[0] == "?":
            time_li[0] = "1" if "4" <= time_li[1] <= "9" else "2"
        if time_li[1] == "?":
            time_li[1] = "9" if time_li[0] == "0" or time_li[0] == "1" else "3"
        if time_li[3] == "?":
            time_li[3] = "5"
        if time_li[4] == "?":
            time_li[4] = "9"
        return "".join(time_li)

if __name__ == "__main__":
    solution = Solution()
    time = "?4:03"
    print(solution.maximumTime(time))
