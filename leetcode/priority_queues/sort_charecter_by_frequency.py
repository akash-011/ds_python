"""
https://leetcode.com/problems/sort-characters-by-frequency
"""


def sort_charecters_by_frequency(s):

    hash_map = {}
    for i in s:
        if i not in hash_map.keys():
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    res = []
    for k, v in sorted(hash_map.items(), key= lambda x: -x[1]):
        res += [k] * v
    return "".join(res)

print(sort_charecters_by_frequency('abba'))