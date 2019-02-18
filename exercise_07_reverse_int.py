# -*- coding: utf-8 -*-
import math
"""
反转整数的数字。 
例1：x = 123，返回321 
例2：x = -123，返回-321 
注意： 假设输入是32位有符号整数。当反向整数溢出时，您的函数应返回0。

"""
# 法一：
class Solution1:
    def _get_int(self, data):
        digit = 1
        res = 0
        for i in data[::-1]:
            res += i * digit
            digit *= 10
        return res

    def reverse(self, x):
        res = []
        digit = 1
        minus = False
        if x < 0:
            minus = True

        tmp = abs(x)
        while tmp > 0:
            res.append(tmp % 10)
            tmp //= 10
        
        result = self._get_int(res)
        if minus:
            result *= -1
        # 注意：2^31-1=2147483647
        if -2**31 < result < 2**31 -1:
            return result
        return 0


# 法二： 
class Solution:
    def reverse(self, x):
        tmp = str(x)
        res = ''
        if tmp.startswith("-"):
            res += '-'
        # if tmp[0] == '-':
        #     res += '-'
        res += tmp[::-1].strip("-")
        res = int(res)
        if -2**31 < res < 2**31-1:
            return res
        return 0


def main():
    s = Solution()
    res = s.reverse(123)
    # res = s.reverse(-123)
    # res = s.reverse(-120)
    # res = s.reverse(-0)
    # res = s.reverse(651121)
    res = s.reverse(1534236469)
    print(res)


if __name__ == "__main__":
    main()
