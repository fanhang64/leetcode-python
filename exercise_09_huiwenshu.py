class Solution:
    def isPalindrome(self, x:str) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        data = str(x)
        index = 0
        length = len(data) - 1  # 2
        while index < length:  # 0 < 2
            if data[index] != data[length]:
               return False
            index += 1
            length -= 1
        return True


class Solution:
    def isPalindrome(self, x:str) -> bool:
        data = str(x)
        rev_data = data[::-1]
        for i in range(len(data)):
            if data[i] != rev_data[i]:
                return False
        return True


class Solution:
    def isPalindrome(self, x:int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        half_reversed = 0
        while x > half_reversed:  # 时间复杂度O(log(n))
            half_reversed = half_reversed * 10 + x % 10
            x //= 10
        
        return x == half_reversed or x == half_reversed // 10
        

class Solution:
    def isPalindrome(self, x) -> bool:
        if x < 0:
            return False
        rev = str(x)
        return rev == rev[::-1]


class Solution:
    def isPalindrome(self, x) -> bool:
        return str(x) == str(x)[::-1]

def main():
    s = Solution()
    res = s.isPalindrome(123)
    # res = s.isPalindrome(1221)
    # res = s.isPalindrome(-121)
    res = s.isPalindrome(101)
    res = s.isPalindrome(121)
    print(res)


if __name__ == "__main__":
    main()
        