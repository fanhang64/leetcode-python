"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
最大子数列问题的目标是在数列的一维方向找到一个连续的子数列，使该子数列的和最大

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""

class Solution:  # 时间复杂度O(n^2)
    def maxSubArray(self, nums: 'List[int]') -> int:
        d = {}
        length = len(nums)
        if length == 1:
            return nums[0]
        max_v = nums[0]
        for i in range(length):
            tmp = nums[i]
            max_v = max([nums[i], max_v])
            for j in range(i+1, length):
                tmp += nums[j]
                if max_v < tmp:
                    max_v = tmp
            # print(tmp)
        return max_v


class Solution1:
    def maxSubArray(self, nums: 'List[int]') -> int:
        max_val = 0
        if len(nums) > 0:
            max_val = nums[0] 
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp > max_val:  # -2 > 1
                max_val = tmp
            
            if tmp < 0:
                tmp = 0
        return max_val


def main():
    s = Solution()
    # res = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    # res = s.maxSubArray([2,4,-7,5,2,-1,2,-4,3])
    # res = s.maxSubArray([1])
    # res = s.maxSubArray([1, 2])
    res = s.maxSubArray([-2, 1])
    # res = s.maxSubArray([2, -20])
    # res = s.maxSubArray([0])
    # res = s.maxSubArray([-2, -3, 2])

    print(res)


if __name__ == "__main__":
    main()
