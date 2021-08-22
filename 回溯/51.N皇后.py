'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]
'''

class Solution:
    def solveNQueens(self, n):
        col = [True for _ in range(n)]
        obleft = [True for _ in range(2 * n - 1)]
        obright = [True for _ in range(2 * n - 1)]

        combinations =[]
        combination = []
        def backTrack(i):
            if i == n:
                combinations.append([''.join(c) for c in combination])
            
            for j in range(n):
                temp = ['.' for _ in range(n)] 
                if col[j] and obleft[i + j] and obright[n - 1 + i - j]:
                    col[j] = obleft[i + j] = obright[n - 1 + i - j] = False
                    temp[j] = 'Q'
                    combination.append(temp)
                    backTrack(i + 1)
                    col[j] = obleft[i + j] = obright[n - 1 + i - j] = True
                    combination.pop()
        backTrack(0)
        return combinations