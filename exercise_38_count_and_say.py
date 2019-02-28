"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
6.     312211
7.     13112221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
1211 一个1,一个2,两个1即 11 12 21
给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"
示例 2:
输入: 4
输出: "1211"
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        if n < 1 or n > 30:
            return '1'
        for x in range(1, n):
            i = 0
            t = ''
            while i < len(res):   #  len(res) == 6
                index = 1
                for j in range(i+1, len(res)):  # 1, 6
                    if res[i] != res[j]:
                        break
                    index += 1  # 3
                t += str(index) + res[i]
                i += index
            res = t
        return res


class Solution:
    def countAndSay(self, n: int) -> str:  # 1211   # 111221
        res = '1'
        result = ''
        for x in range(1, n):
            result = ''
            ch = res[0]
            count = 0
            for i in range(len(res)):
                if ch == res[i]:
                    count += 1
                else:
                    result = result + str(count) + ch
                    count = 1
                    ch = res[i]
            result = result + str(count) + ch
            res = result
        return res


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(1, n):
            result = self.say(result)
        return result
    
    def say(self, in_str):
        out = ""
        count = 0
        ch = in_str[0]
        for i in range(len(in_str)):
            if ch == in_str[i]:
                count += 1
            else:
                out = out + str(count) + ch
                count = 1
                ch = in_str[i]
        out = out + str(count) + ch
        return out


class Solution:  # 参考。。
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import re
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s))
        return s


def main():
    s = Solution()
    # res = s.countAndSay(2)
    # res = s.countAndSay(4)
    res = s.countAndSay(5)
    print(res)


if __name__ == "__main__":
    main()
