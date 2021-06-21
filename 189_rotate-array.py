"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

测试用例：
nums = [1,2,3,4,5,6,7] : [5,6,7,1,2,3,4]
nums = [-1,-100,3,99] : [3,99,-1,-100]

解题思路：使用额外数组，环状替换，数组翻转，环形旋转
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        使用额外的数组
        我们可以使用额外的数组来将每个元素放至正确的位置。
        用n表示数组的长度，我们遍历原数组，将原数组下标为i的元素放至新数组下标为 (i+k) mod n 的位置，最后将新数组拷贝至原数组即可。
        时间复杂度： O(n)，其中 nn 为数组的长度。空间复杂度： O(n)。
        """
        length = len(nums)
        nums1 = [0 for i in range(0,length)]
        for i in range(0, length):
            nums1[(i+k)%length] = nums[i]
        nums = nums1

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        环状替换
        方法一中使用额外数组的原因在于如果我们直接将每个数字放至它最后的位置，这样被放置位置的元素会被覆盖从而丢失。
        因此，从另一个角度，我们可以将被替换的元素保存在变量 temp 中，从而避免了额外数组的开销。
        我们从位置 0 开始，最初令temp=nums[0]。根据规则，位置 0 的元素会放至 (0+k)modn 的位置，令 x=(0+k)modn，此时交换 temp 和 nums[x]，完成位置 x 的更新。
        然后，我们考察位置 x，并交换temp 和nums[(x+k)modn]，从而完成下一个位置的更新。
        不断进行上述过程，直至回到初始位置 0。
        容易发现，当回到初始位置 0 时，有些数字可能还没有遍历到，此时我们应该从下一个数字开始重复的过程，可是这个时候怎么才算遍历结束呢？
        我们不妨先考虑这样一个问题：从 0 开始不断遍历，最终回到起点 0 的过程中，我们遍历了多少个元素？
        由于最终回到了起点，故该过程恰好走了整数数量的圈，不妨设为 a 圈；再设该过程总共遍历了 b 个元素。因此，我们有 an=bk，即 an 一定为 n,kn,k 的公倍数。
        又因为我们在第一次回到起点时就结束，因此 a 要尽可能小，故 an 就是 n,kn,k 的最小公倍数lcm(n,k)，因此 b 就为 lcm(n,k)/k。
        这说明单次遍历会访问到 lcm(n,k)/k 个元素。为了访问到所有的元素，我们需要进行遍历的次数为n/(lcm(n,k)/k) = nk/(lcm(n,k)) = gcd(n,k), 其中gcd 指的是最大公约数。
        时间复杂度：O(n)O(n)，其中 nn 为数组的长度。每个元素只会被遍历一次。
        空间复杂度：O(1)O(1)。我们只需常数空间存放若干变量。
        如果读者对上面的数学推导的理解有一定困难，也可以使用另外一种方式完成代码：使用单独的变量 count 跟踪当前已经访问的元素数量，当 count=n 时，结束遍历过程。
        无法理解。。。
        """
        length = len(nums)
        k %= length
        start = 0
        n = length
        while start < length and k != 0:
            for i in range(0, k):
                nums[start+i], nums[length-k+i] = nums[length-k+i], nums[start+i]
            start += k
            n -= k
            k %= n

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        数组翻转
        该方法基于如下的事实：当我们将数组的元素向右移动 k 次后，尾部 kmodn 个元素会移动至数组头部，其余元素向后移动 kmodn 个位置。
        该方法为数组的翻转：我们可以先将所有元素翻转，这样尾部的 kmodn 个元素就被移至数组头部，然后我们再翻转 [0,kmodn−1] 区间的元素和 [kmodn,n−1] 区间的元素即能得到最后的答案。
        """
        k %= len(nums)
        if len(nums) <= 1:
            return
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        环形旋转，即环状替换的循环方式，直到回到0位置。
        特殊情况：如果nums.length%k=0，也就是数组长度为k的倍数，这个会原地打转
        对于这个问题我们可以使用一个数组visited表示这个元素有没有被访问过，如果被访问过就从他的下一个开始，防止原地打转。
        """
        hold = nums[0]
        index = 0
        length = len(nums)
        visited = [False for i in range(0, length)]
        for i in range(0, length):
            index = (index + k) % length
            if visited[index]:
                index = (index + 1) % length
                hold = nums[index]
                i -= 1
            else:
                nums[index], hold = hold, nums[index]
                visited[index] = True

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate3(nums, k)
    print(nums)








