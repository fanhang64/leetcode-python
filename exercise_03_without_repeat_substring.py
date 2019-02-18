# -*- coding: utf-8 -*-
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

"""
# TODO

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         i, j = 0, 0
#         length = len(s)
#         max_length = 0
#         tmp = []
#         index = 0
#         for x in range(length):
#             for y in range(x+1, length):
#                 if s[y] in tmp:
#                     index = 0
#                     tmp = []
#                 tmp.append(x)
#                 index += 1
#                 if index > max_length:
#                     max_length = index
#         return max_length


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         length = len(s)
#         tmp = []
#         max_length = 0

#         for x in range(length):
#             tmp.append(s[x])

#             index = 0
#             for y in range(x+1, length):
#                 index += 1
#                 if index > max_length:
#                     max_length = index
#                 if s[y] in tmp:
#                     print(tmp)
#                     tmp = []
#                     break
#                 tmp.append(s[y])
#                 if s[y] == s[length-1]:
#                     return max_length
#         return max_length


# def main():
#     s = Solution()
#     res = s.lengthOfLongestSubstring("abcabcbb")
#     # res = s.lengthOfLongestSubstring("abc")
#     # res = s.lengthOfLongestSubstring("fanzone")
#     # res = s.lengthOfLongestSubstring("  a")
#     # res = s.lengthOfLongestSubstring("localhost")
#     # res = s.lengthOfLongestSubstring("")
#     # res = s.lengthOfLongestSubstring("dvdf")
#     print(res)


# if __name__ == "__main__":
#     main()