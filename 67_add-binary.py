"""
67.二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。
解题思路：相加后有三种情况：0,1,2,3;addBinary1比addBinary运行时间更少，更好。最后addBinary2是最好的，但比较没意思
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = list(a)
        b_list = list(b)
        i = len(a_list) - 1
        j = len(b_list) - 1
        result = ""
        pre = 0
        while i >= 0 and j >= 0:
            sum = int(a_list[i]) + int(b_list[j]) + pre
            if sum == 1:
                result = "1" + result
                pre = 0
            elif sum == 2:
                result = "0" + result
                pre = 1
            elif sum == 3:
                result = "1" + result
                pre = 1
            else:
                result = "0" + result
                pre = 0
            i -= 1
            j -= 1
        while i >= 0:
            sum = int(a_list[i]) + pre
            if sum == 1:
                result = "1" + result
                pre = 0
            elif sum == 2:
                result = "0" + result
                pre = 1
            else:
                result = "0" + result
                pre = 0
            i -= 1
        while j >= 0:
            sum = int(b_list[j]) + pre
            if sum == 1:
                result = "1" + result
                pre = 0
            elif sum == 2:
                result = "0" + result
                pre = 1
            else:
                result = "0" + result
                pre = 0
            j -= 1
        if pre == 1:
            result = "1" + result
        return result

    def addBinary1(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        c = 0
        result = ""
        while i >= 0 or j >= 0:
            if i >= 0:
                c += int(a[i])
            if j >= 0:
                c += int(b[j])
            result = str(c % 2) + result
            c = int(c/2)
            i -= 1
            j -= 1
        return "1" + result if c else result


    def addBinary2(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    solution = Solution()
    a = "1010"
    b = "1011"
    a = "0"
    b = "0"
    a = "11"
    b = "1"
    print(solution.addBinary1(a, b))