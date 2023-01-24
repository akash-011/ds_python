"""
https://leetcode.com/problems/search-insert-position/description/
st
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
# binary search os 0(log N)

def serach_insert_postion(nums, target):
    x =0
    y = len(nums) - 1

    while x <= y:
        mid = (x + y) // 2
        if (nums[mid] == target):
            return mid
        elif target > nums[mid]: 
            x = mid + 1
        else:
            y = mid -1 

    return x 
