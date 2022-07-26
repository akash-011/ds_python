"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
"""

# https://leetcode.com/problems/remove-element/

def solution_1(nums, val):
    while val in nums:
        nums.remove(val)

