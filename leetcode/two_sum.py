"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

https://leetcode.com/problems/two-sum/
"""


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum_better(nums, target):
    my_dict = {}
    for i, v in enumerate(nums):
        remainder = target - v
        if remainder in my_dict:
            return [my_dict[remainder], i]
        my_dict[v] = i