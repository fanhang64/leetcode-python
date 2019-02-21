# coding: utf-8

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        for i in range(0, len(strs)-1):
            tmp = ""
            if i == 0:  # 第一次取两个元素
                x, y = strs[i], strs[i+1]
            else:  # 其余取前一次比较结果作为下次的元素比较
                x, y = res, strs[i+1]
            len_min = min(len(x), len(y))
            for i in range(len_min):
                if x[i] != y[i]:
                    break
                tmp += x[i]
            res = tmp
        return res


# 纵向扫描法：从下标0开始，判断每一个字符串的下标0，判断是否全部相同。
# 直到遇到不全部相同的下标。时间性能为O(n*m)。
# ["abc", "abd", "abcd"]
# ["123", "124", "15", "126"]
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        str_len = len(strs)
        if str_len == 0:
            return ""
        if str_len == 1:
            return strs[0]
        res = ""        
        first = strs[0]
        first_len = min(len(i) for i in strs)
        for i in range(0, first_len): # ["aa", "a"]
            for j in range(1, str_len):
                if first[i] != strs[j][i]:
                    return res
            res += first[i]
        return res
            

def main():
    s = Solution()
    # res = s.longestCommonPrefix(["flower","flow","flight"])
    # res = s.longestCommonPrefix(["dog","dracecar","dcar"])
    # res = s.longestCommonPrefix(["123", "124", "125", "126"])
    # res = s.longestCommonPrefix(["1"])
    res = s.longestCommonPrefix(["aa", "a"])
    print(res)


if __name__ == "__main__":
    main()
