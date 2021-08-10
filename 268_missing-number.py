"""
268.丢失的数字
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?
解题思路：位运算; 数学
位运算：
    由于异或运算（XOR）满足交换律和结合律，并且对一个数进行两次完全相同的异或运算会得到原来的数，因此我们可以通过异或运算找到缺失的数字。
    我们知道数组中有 n 个数，并且缺失的数在 [0..n] 中。
    因此我们可以先得到 [0..n] 的异或值，再将结果对数组中的每一个数进行一次异或运算。
    未缺失的数在 [0..n] 和数组中各出现一次，因此异或后得到 0。
    而缺失的数字只在 [0..n] 中出现了一次，在数组中没有出现，因此最终的异或结果即为这个缺失的数字。
数学：
    我们可以用 高斯求和公式 求出 [0..n] 的和，减去数组中所有数的和，就得到了缺失的数字。
    高斯求和公式即 sum = n*(n+1)/2
"""
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        位运算
        时间击败60.79%，内存击败21.12%
        """
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result

    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        数学
        时间击败75.99%，内存击败26.59%
        """
        return len(nums)*(len(nums)+1)/2 - sum(nums)