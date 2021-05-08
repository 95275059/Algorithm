"""
给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

解题思路：动态规划；贪心算法

一、动态规划：
1.定义dp[i][0]表示第i+1天交易完之后手里没有股票的最大利润，dp[i][1]表示第i+1天交易完之后手里持有股票的最大利润。
2.当天交易完之后手里没有股票可能有两种情况
  一种是当天没有进行任何交易，又因为当天手里没有股票，所以当天没有股票的利润只能取前一天手里没有股票的利润。
  一种是把当天手里的股票给卖了，既然能卖，说明手里是有股票的，所以这个时候当天没有股票的利润要取前一天手里有股票的利润加上当天股票能卖的价格。
  这两种情况我们取利润最大的即可，所以可以得到：dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i]);
3.当天交易完之后手里持有股票也有两种情况
  一种是当天没有任何交易，又因为当天手里持有股票，所以当天手里持有的股票其实前一天就已经持有了。
  还一种是当天买入了股票，当天能买股票，说明前一天手里肯定是没有股票的，
  我们取这两者的最大值，所以可以得到：dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i]);
3.动态规划的递推公式有了，那么边界条件是什么，就是第一天
  如果买入：dp[0][1]=-prices[0];
  如果没买：dp[0][0]=0;

代码优化：
上面计算的时候我们看到当天的利润只和前一天有关，没必要使用一个二维数组，
只需要使用两个变量，一个记录当天交易完之后手里持有股票的最大利润，一个记录当天交易完之后手里没有股票的最大利润

二、贪心算法：
如果股票一直上涨，只需要找到股票上涨的最大值和股票开始上涨的最小值，计算他们的差就是这段时间内股票的最大利润。
如果股票下跌就不用计算，最终只需要把所有股票上涨的时间段内的利润累加就是我们所要求的结果
贪心算法是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，算法得到的是在某种意义上的局部最优解。
那么这道题使用贪心算法也是最容易解决的，只要是上涨的我们就要计算他们的差值进行累加，不需要再找开始上涨的最小值和最大值。


"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        dp = []
        dp.append([0, -prices[0]])
        for i in range(1, len(prices)):
            dp0 = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp1 = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp.append([dp0, dp1])
        return dp[len(prices)-1][0]

    def maxProfit2(self, prices):
        # 执行用时：16ms, 在所有Python提交中击败了96.20 %的用户
        # 内存消耗：13.9MB, 在所有Python提交中击败了33.21 %的用户
        if len(prices) <= 1:
            return 0
        hold = -prices[0]
        nohold = 0
        for i in range(1, len(prices)):
            hold = max(hold, nohold - prices[i])
            nohold = max(nohold, hold + prices[i])
        return nohold

    def maxProfit3(self, prices):
        length = len(prices)
        if length <= 1:
            return 0
        profit = 0
        index = 0
        while index < length:
            # 如果股票下跌就一直找，直到找到股票开始上涨为止
            while index < length - 1 and prices[index] >= prices[index + 1]:
                index += 1
            # 股票上涨开始的值，也就是这段时间上涨的最小值
            min_price = prices[index]
            # 一直找到股票上涨的最大值为止
            while index < length - 1 and prices[index] <= prices[index + 1]:
                index += 1
            # 计算这段上涨时间的差值，然后累加
            profit += prices[index] - min_price
        return profit

    def maxProfit4(self, prices):
        # 执行用时：20ms, 在所有Python提交中击败了86.99 %的用户
        # 内存消耗：13.9MB, 在所有Python提交中击败了47.47 %的用户
        length = len(prices)
        if length <= 1:
            return 0
        profit = 0
        for i in range(0, length - 1):
            profit += max(prices[i+1] - prices[i], 0)
        return profit



if __name__ == '__main__':
    solution = Solution()
    #prices = [7,1,5,3,6,4]
    #prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    print(solution.maxProfit(prices))