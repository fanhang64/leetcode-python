"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = s.strip(" ").split(" ")[-1]
        return len(last_word)


class Solution:
    def lengthOfLastWord(self, s) -> int:
        cnt = 0
        for i in s[::-1].strip(" "):
            if i == ' ':
                break
            cnt += 1
        return cnt


def main():
    s = Solution()
    res = s.lengthOfLastWord("Hello World")
    # res = s.lengthOfLastWord("hello")
    # res = s.lengthOfLastWord("")
    # res = s.lengthOfLastWord("a")
    # res = s.lengthOfLastWord(" ")
    # res = s.lengthOfLastWord("a ")
    res = s.lengthOfLastWord(" a b c de fgh ")
    print(res)


if __name__ == "__main__":
    main()
