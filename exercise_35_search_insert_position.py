"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
"""

class Solution:
    def searchInsert(self, nums:'List[int]', target: int) -> int:
        position = 0
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if nums[i] == target:
                position = i
                break
            if nums[i] < target:
                position = i + 1
        return position


class Solution:
    def searchInsert(self, nums:'List[int]', target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


def main():
    s = Solution()
    # res = s.searchInsert([1,3,5,6], 5)
    # res = s.searchInsert([1,3,5,6], 2)
    res = s.searchInsert([1,3,5,6], 7)
    # res = s.searchInsert([1,3,5,6], 0)
    # res = s.searchInsert([], 1)
    print(res)


if __name__ == "__main__":
    main()
