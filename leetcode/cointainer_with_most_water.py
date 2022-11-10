"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

link : https://leetcode.com/problems/container-with-most-water/
"""


def maxArea(height):
    area = 0
    start = 0
    end = len(height) - 1

    if len(height) == 2:
        return min(height)

    while start < end:
        min_height = min(height[start], height[end])
        area = max(area, (min_height * (end-start)))
        print(area)
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return area

maxArea([4,3,2,1,4])