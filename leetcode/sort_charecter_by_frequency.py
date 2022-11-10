"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

https://leetcode.com/problems/sort-characters-by-frequency
"""

import collections
import heapq


def sort_characters_by_frequency(s):

    hash_map = {}
    for i in s:
        if i not in hash_map.keys():
            hash_map[i] = 1
        else:
            hash_map[i] += 1
    res = []
    for k, v in sorted(hash_map.items(), key= lambda x: x[1], reverse=True):
        res += [k] * v
    return "".join(res)


def sort_chars_by_freq(s):
    """Use a priority queue"""
    cnt = collections.Counter(s)
    pq = [(-v,k) for k, v in cnt.items()]
    heapq.heapify(pq)
    print(pq)

    res= []
    while pq:
        v, k = heapq.heappop(pq)
        res += [k] * -v
    return ''.join(res)


print(sort_chars_by_freq('abbafkkkij'))