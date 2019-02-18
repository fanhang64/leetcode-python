# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

# 解法1, 时间复杂度O(n^2)
class Solution1:
    def twoSum(self, nums, target):
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    continue
                if x + y == target:
                    return i, j

# 解法2, 时间复杂度O(n^2)
class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return i, j

# 解法3 
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for index, i in enumerate(nums):
            res = target - i
            for k, v in d.items():
                if res == v:
                    return k, index
            d[index] = i 

# 解法4 两遍hash
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for k,v in enumerate(nums):
            d[v] = k
        for i in range(len(nums)):
            res = target - nums[i]
            if res in d and d.get(res) !=i:
                return i, d[res]


# 解法5 
class Solution:
    def twoSum(self, nums, target):
        d = {}
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res in d:
                return d.get(res), i
            d[nums[i]] = i 


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    # nums = [3, 2, 4]
    # target = 6
    # nums = [3, 3]
    # target = 6
    # nums = [3, 3, 3, 3]
    # target = 6
    # nums = [3, 2, 3]
    # target = 6

    s = Solution()
    res = s.twoSum(nums, target)
    print(res)
