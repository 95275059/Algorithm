"""
217.存在重复元素
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

解题思路：哈希表；排序
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        哈希表
        时间击败6.58%，内存击败96.31%
        """
        result = False
        map = []
        for n in nums:
            if n in map:
                result = True
                break
            else:
                map.append(n)
        return result

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        排序
        时间击败44.46%，内存击败85.91%
        """
        result = False
        nums.sort()
        if not len(nums):
            return result
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                result = True
                break
        return result

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,1]
    #nums = [1, 2, 3, 4]
    #nums = [1,1,1,3,3,4,3,2,4,2]
    #nums = []
    result = solution.containsDuplicate1(nums)
    print(result)