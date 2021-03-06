'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

示例 2：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
'''

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[right][mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        
        return matrix[right][r] == target
