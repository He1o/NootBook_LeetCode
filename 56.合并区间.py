'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。


示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

'''
class Solution:
    # 原本想用分治的算法，结果并不可以
    def merge(self, intervals):
        intervals = sorted(intervals, key = lambda x: x[0])

        def dc(i, j):
            if i == j:
                return [intervals[i]]
            
            mid = (i + j) // 2
            left = dc(i, mid)
            right = dc(mid + 1, j)

            l1, l2 = left[-1], right[0]
            if l2[0] <= l1[1]:
                if l2[1] <= l1[1]:
                    left[-1] = l1
                    right.pop(0)
                    left.extend(right)
                    return left
                else:
                    left[-1] = [l1[0], l2[1]]
                    right.pop(0)
                    left.extend(right)
                    return left
            else:
                left.extend(right)
                return left

        return dc(0, len(intervals) - 1)

    # 不用分治就没什么难度了，先排序我也想到了
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged



s = [[2,3],[4,5],[6,7],[8,9],[1,10]]
S = Solution()   
re = S.merge(s)
print(re)    

