"""
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
实现 Solution class:
    Solution(int[] nums) 使用整数数组 nums 初始化对象
    int[] reset() 重设数组到它的初始状态并返回
    int[] shuffle() 返回数组随机打乱后的结果
解题思路：暴力；洗牌算法
暴力
    假设我们把每个数都放在一个 ”帽子“ 里面，然后我们从帽子里面把它们一个个摸出来，摸出来的数按顺序放入数组，这个数组正好就是我们要的洗牌后的数组。
    暴力算法简单的来说就是把每个数放在一个 ”帽子“ 里面，每次从 ”帽子“ 里面随机摸一个数出来，直到 “帽子” 为空。
    下面是具体操作：
        首先我们把数组 array 复制一份给数组 aux，之后每次随机从 aux 中取一个数
        为了防止数被重复取出，每次取完就把这个数从 aux 中移除。
        重置 的实现方式很简单，只需把 array 恢复称最开始的状态就可以了。
洗牌算法
    我们可以用一个简单的技巧来降低之前算法的时间复杂度和空间复杂度，那就是让数组中的元素互相交换，这样就可以避免掉每次迭代中用于修改列表的时间了。
    Fisher-Yates 洗牌算法跟暴力算法很像。
    在每次迭代中，生成一个范围在当前下标到数组末尾元素下标之间的随机整数。
    接下来，将当前元素和随机选出的下标所指的元素互相交换
        - 这一步模拟了每次从 “帽子” 里面摸一个元素的过程，其中选取下标范围的依据在于每个被摸出的元素都不可能再被摸出来了。
    此外还有一个需要注意的细节，当前元素是可以和它本身互相交换的 - 否则生成最后的排列组合的概率就不对了。
"""
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = list(nums)
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        暴力， 洗牌算法
        """
        self.array = self.origin
        self.origin = list(self.origin)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        暴力
        时间击败76.09%，内存击败10.87%
        """
        anx = list(self.array)
        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(anx))
            self.array[idx] = anx.pop(remove_idx)
        return self.array

    def shuffle1(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        洗牌算法
        时间击败21.74%，内存击败41.85%
        """
        length = len(self.array)
        for idx in range(length-1):
            change_index = random.randrange(idx, length)
            self.array[idx], self.array[change_index] = self.array[change_index], self.array[idx]
        return self.array



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()