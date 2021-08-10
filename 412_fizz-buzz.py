"""
412.Fizz Buzz
写一个程序，输出从 1 到 n 数字的字符串表示。
    1. 如果n是3的倍数，输出“Fizz”；
    2. 如果n是5的倍数，输出“Buzz”；
    3. 如果n同时是3和5的倍数，输出 “FizzBuzz”。
解题思路：模拟法；字符串连接；散列表
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        :param n:
        :return:
        模拟法
        就像你每次玩 FizzBuzz 那样，你只需要判断这个数是能被 3 整除？ 还是能被 5 整除？ 或者是都能被整除。
            初始化一个空的答案列表。
            遍历 1 ... N1...N。
            对于每个数，判断它能不能同时被 3 和 5 整除，如果可以就把 FizzBuzz 加入答案列表。
            如果不行，判断它能不能被 3 整除，如果可以，把 Fizz 加入答案列表。
            如果还是不行，判断它能不能被 5 整除，如果可以，把 Buzz 加入答案列表。
            如果以上都不行，把这个数加入答案列表。
        时间击败62.51%，内存击败8.54%
        """
        result = list()
        for num in range(1, n+1):
            devide_by_3 = (num%3 == 0)
            devide_by_5 = (num%5 == 0)
            if devide_by_5 and devide_by_3:
                result.append("FizzBuzz")
            elif devide_by_3:
                result.append("Fizz")
            elif devide_by_5:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result
    def fizzBuzz1(self, n: int) -> List[str]:
        """
        :param n:
        :return:
        字符串拼接
        这个方法不会降低渐进复杂度，但是当 FizzBuzz 的规则变得更复杂的时候，这将会是个更优雅的解法。
            玩个 FizzBuzzJazz 的游戏。规则如下：3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
            如果你还是用之前的方法来解决这个问题的话，那将会有非常多的条件需要判断哦~
        我们放弃使用之前的联合判断，取而代之依次判断是否能被给定的数整数。
        这道题中，就是依次判断能不能被 3 整除，能不能被 5 整除。
        如果能被 3 整除，就把对应的 Fizz 连接到答案字符串，如果能被 5 整除，就把 Buzz 连接到答案字符串。
        对于 FizzBuzz 来说，只需要判断两个条件就可以了，而不需要像方法一中那样判断三个条件。
        时间击败82.45%，内存击败14.55%
        """
        result = list()
        for num in range(1, n+1):
            devide_by_3 = (num%3 == 0)
            devide_by_5 = (num%5 == 0)
            strr = ""
            if devide_by_3:
                strr += "Fizz"
            if devide_by_5:
                strr += "Buzz"
            if strr == "":
                strr = str(num)
            result.append(strr)
        return result

    def fizzBuzz2(self, n: int) -> List[str]:
        """
        :param n:
        :return:
        散列表
        这个方法是对方法二的优化。
        当数字和答案的映射是定好的，那么方法二用起来也还可以。
        但是如果你遇到一个变态的面试官，他跟你说他需要更自由的映射关系呢？
        每个映射一个判断显然是不可行的，这样写出来的代码一定是丑陋不堪且难以维护的。
        如果老板有这样一个需求，明天你把映射关系换掉或者删除一个映射关系吧。对于这种要求，我们只能一个个去修改判断条件的代码。
        但我们实际上有个更优雅的做法，那就是把映射关系放在 散列表 里面。
            把所有的映射关系放在散列表 fizzBuzzHash 中，这个散列表形如 { 3: 'Fizz', 5: 'Buzz' }。
            遍历 1 ... N1...N。
            对于每个数字，遍历 fizzBuzzHash 中的键，检查是否能被它整除。
            如果这个数能被键整除，就把当前键映射的值加到到答案字符串后面去。对于散列表的每个键值对，都这样操作。
            最后将答案字符串加入答案列表。
        时间击败62.51%，内存击败33.26%
        """
        result = list()
        dic = {3: "Fizz", 5: "Buzz"}
        for num in range(1, n+1):
            strr = ""
            for key, value in dic.items():
                if num % key == 0:
                    strr += value
            if strr == "":
                strr = str(num)
            result.append(strr)
        return result