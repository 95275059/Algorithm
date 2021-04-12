"""
66.加一
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[0] == 0:
            return [1]
        else:
            result = digits
            result[-1] += 1
            i = len(result) - 1
            while i > 0:
                if result[i] == 10:
                    result[i] = 0
                    result[i - 1] += 1
                i -= 1
            if result[0] == 10:
                result[0] = 0
                return [1] + result
            else:
                return result

    def plusOne1(self, digits):
        """
        逢9进位，否则当前位+1后直接return
        """
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits
    def plusOne2(self, digits):
        """
        先把列表转化为字符串，然后转化为整数再加一，再把数字转化为列表
        """
        return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

if __name__ == '__main__':
 solution = Solution()
 digits = [1, 2, 3]
 digits = [4, 3, 2, 1]
 digits = [0]
 digits = [9, 9, 9]
 print(solution.plusOne(digits))