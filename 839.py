# 题目：
# 如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。
# 如果这两个字符串本身是相等的，那它们也是相似的。
# 例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)； "rats" 和 "arts" 也是相似的，
# 但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
# 总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。
# 注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
# 形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
# 给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。
# 请问 strs 中有多少个相似字符串组？
# 实例
# 输入：strs = ["tars","rats","arts","star"]
# 输出：2

# 思路：
# 相似字符串组中的每个字符串都有另外至少一个字符串和它相似。
# 比如对于 {"tars", "rats", "arts"} 这个相似字符串组而言，
# 相似关系是 "tars" <=> "rats" <=> "arts" 。

# 两个字符串相似的含义是能够通过交换两个字符的位置，得到另外一个字符串。
# 判断两个字符串相似的时间的复杂度是 O(N)，因为把所有位置遍历一次，统计两个字符串的对应位置有多少不等即可。

# 明白了题意之后，做法也就呼之欲出了：把每个字符串当做图中的一个节点，
# 如果两个字符串相似，那么它们之间就有一条边。
# 图中的每个连通区域是一个相似字符串组。问：图中有多少个不连通的区域？

from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        N = len(strs)
        dsu = DSU(N)
        for i in range(N):
            for j in range(i + 1, N):
                if self.isSimilar(strs[i], strs[j]):
                    dsu.union(i, j)
        return dsu.regions()
        
    def isSimilar(self, str1, str2):
        count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count += 1
        return count == 2 or count == 0


# 并查集的思路：1、初始化每一个元素单独都是一个类别，类别的编号是父节点或者par，共有初始化regions = N个类别。
# 2、然后判断节点是否连接，如果是相连的则用union把这两个节点连接起来，共用同一个par，同时类别数regions = N。
# 3、find函数是找到最终的父节点，也就是类别编号
# 4、最后剩下的regions，就是可以分成的类别数量。
class DSU:
    def __init__(self, N):
        self.par_ = list(range(N+1))
        self.regions_ = N
    
    def find(self, x):
        if x!= self.par_[x]:
            self.par_[x] = self.find(self.par_[x])
        return self.par_[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return 
        self.par_[px] = py
        self.regions_ -= 1

    def regions(self):
        return self.regions_

sol = Solution()
output = sol.numSimilarGroups(['asd','dsa','ads'])
print(output)