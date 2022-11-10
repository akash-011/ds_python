"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""
import heapq


def maxProduct(nums) :
    nums.sort(reverse=True)
    return (nums[0] - 1) * (nums[1] - 1)


def max_product_2(nums):
    a, b = heapq.nlargest(2, nums)
    return (a-1) * (b-1)
