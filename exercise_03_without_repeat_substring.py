# -*- coding: utf-8 -*-

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


class Solution:
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        tmp = []
        max_length = 0

        for x in range(length):
            tmp.append(s[x])

            index = 0
            for y in range(x+1, length):
                index += 1
                if index > max_length:
                    max_length = index
                if s[y] in tmp:
                    print(tmp)
                    tmp = []
                    break
                tmp.append(s[y])
                if s[y] == s[length-1]:
                    return max_length
        return max_length


def main():
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    # res = s.lengthOfLongestSubstring("abc")
    # res = s.lengthOfLongestSubstring("fanzone")
    # res = s.lengthOfLongestSubstring("  a")
    # res = s.lengthOfLongestSubstring("localhost")
    # res = s.lengthOfLongestSubstring("")
    # res = s.lengthOfLongestSubstring("dvdf")
    print(res)


if __name__ == "__main__":
    main()