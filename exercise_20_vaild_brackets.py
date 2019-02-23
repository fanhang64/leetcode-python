"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true


"""
class Solution:  # TODO {[]} "" 返回的false
    res = []
    def isValid(self, s: 'str') -> 'bool':
        for i in s:
            if i in ('(', '{', '['):
                self.res.append(i)
            else:
                top = self.res.pop() if self.res else ''
                if i == '}' and top == '{':
                    continue
                if i == ']' and top == '[':
                    continue
                if i == ')' and top == '(':
                    continue
                return False
        return not self.res


class Solution1:  # {[]}
    def isValid(self, s) -> 'bool':
        d = {')': '(', '}': '{', ']': '['}
        r = []
        for i in s:
            if i in d:
                top = r.pop() if r else ''
                if d[i] != top:
                    return False 
            else:
                r.append(i)
        return not r


def main():
    s = Solution()
    # res = s.isValid("(){}")
    # res = s.isValid("()[]{}")
    # res = s.isValid("(]")
    # res = s.isValid("([)]")
    # res = s.isValid("[")
    # res = s.isValid("")
    # res = s.isValid("]")
    # res = s.isValid('{[]}')
    # res = s.isValid("(((((())))))")
    # res = s.isValid("[][][]")
    print(res)


if __name__ == "__main__":
    main()
