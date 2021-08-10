"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。
示例：
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

解题思路：
1.两次二分搜索：
    由于每行的第一个元素大于前一行的最后一个元素，且每行元素是升序的，所以每行的第一个元素大于前一行的第一个元素，因此矩阵第一列的元素是升序的。
    我们可以对矩阵的第一列的元素二分查找，找到最后一个不大于目标值的元素，然后在该元素所在行中二分查找目标值是否存在。
2.一次二分查找
    若将矩阵每一行拼接在上一行的末尾，则会得到一个升序数组，我们可以在该数组上二分找到目标元素。
    代码实现时，可以二分升序数组的下标，将其映射到原矩阵的行和列上。
值得注意的是，若二维数组中的一维数组的元素个数不一，方法二将会失效，而方法一则能正确处理
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        两次二分搜索
        时间击败62.95%，内存击败15.94%
        """
        def searchrow(start, end):
            if start > end:
                return -1
            mid = start + (end-start)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif target < matrix[mid][0]:
                return searchrow(start, mid-1)
            else:
                return searchrow(mid+1, end)

        def searchcolumn(row, start, end):
            if start > end:
                return False
            mid = start + (end-start)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                return searchcolumn(row, start, mid-1)
            else:
                return searchcolumn(row, mid+1, end)

        row = searchrow(0, len(matrix)-1)
        if row == -1:
            return False
        else:
            return searchcolumn(row, 0, len(matrix[row])-1)

    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        一次二分搜索
        时间击败62.95%，内存击败13.28%
        """
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n - 1
        while low <= high:
            mid = low + (high - low) // 2
            x = matrix[mid // n][mid % n]
            if x > target:
                high = mid - 1
            elif x < target:
                low = mid + 1
            else:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 33
    print(solution.searchMatrix(matrix, target))