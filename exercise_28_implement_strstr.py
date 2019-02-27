"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "heallo", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        index = 0
        if not needle:
            return 0
        if len(needle) == 1 and haystack == needle:
            return 0
        length = len(haystack)
        while i < length:
            if index == len(needle):
                break
            if haystack[i] == needle[index]:
                index += 1
            else:
                i -= index
                index = 0
            i += 1    
        if index == len(needle):
            return i-index
        return -1


class Solution:  # 不推荐
    def strStr(self, haystack: str, needle: str) -> int:
       return haystack.find(needle)


def main():
    s = Solution()
    res = s.strStr("heallo", "ll")
    # res = s.strStr("aaaaa", "baa")
    # res = s.strStr("s", "s")
    # res = s.strStr("abc", "c")
    # res = s.strStr("mississippi", "issip")  
    res = s.strStr("a", "abc")
    print(res)


if __name__ == "__main__":
    main()
