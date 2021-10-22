'''
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
'''

class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s3) != len(s1) + len(s2):
            return False
        if len(s2) == 0:
            return s1 == s3
        if len(s1) == 0:
            return s2 == s3


        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        for i in range(len(s1)):
            dp[i + 1][0] = dp[i][0] if s1[i] == s3[i] else False
        for i in range(len(s2)):
            dp[0][i + 1] = dp[0][i] if s2[i] == s3[i] else False


        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] | dp[i][j + 1])
                if s2[j] == s3[i + j + 1]:
                    dp[i + 1][j + 1] = (dp[i + 1][j + 1] | dp[i + 1][j])

        return dp[-1][-1]        



# 省略写法
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 动态规划，用dp[i][j]表示，s1的前i个字符即s1[:i]与s2的前j个字符s2[:j]，可以构成s3的前i + j个字符即s3[:i + j]
        n1, n2, n3 = len(s1), len(s2), len(s3)
        # 长度不等时无法得到
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        # 初始化
        dp[0][0] = True

        for i in range(n1 + 1):
            for j in range(n2 + 1):
                # 当s1的第i个字符与s3的第i + j个字符相等时，进行转移
                if i - 1 >= 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                # s2同理
                if j - 1 >= 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        
        return dp[n1][n2]


s1 = "ab"
s2 = "bc"
s3 = "bbac"
S = Solution()   
re = S.isInterleave(s1, s2, s3)
print(re)    



