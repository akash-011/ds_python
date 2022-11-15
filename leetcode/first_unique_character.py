"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

def firstUniqChar(self, s: str) -> int:
    my_dict = {}

    for c in s:
        my_dict[c] = my_dict.get(c, 0) + 1

    for i, c in enumerate(s):
        if my_dict[c] == 1:
            return i
    return -1
    