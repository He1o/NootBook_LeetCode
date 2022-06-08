'''
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        def generateTree(start, end):
            if start >= end:
                return [None]
            
            result = []
            for i in range(start, end):
                left_trees = generateTree(start, i)
                right_trees = generateTree(i + 1, end)
                
                for left in left_trees:
                    for right in right_trees:
                        currTree = TreeNode(i + 1)  #   注意放置位置，放在前面不久被覆盖了，有重复数据，注意是不是重复传入指针
                        currTree.left = left
                        currTree.right = right
                        result.append(currTree)
            return result
        return generateTree(0, n)

s = Solution()
re = s.generateTrees(3)
print(re)



