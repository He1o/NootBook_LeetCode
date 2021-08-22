'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：
输入：digits = [0]
输出：[1]

'''

class Solution:
    def plusOne(self, digits):

        digits[-1] += 1
        add = 0
        for i in range(len(digits) - 1, -1, -1):
            x = digits[i] + add
            digits[i] = x % 10
            add = x // 10

        if add:
            digits = [add] + digits
        return digits

s = [9,9,9]
S = Solution()   
re = S.plusOne(s)
print(re)        
