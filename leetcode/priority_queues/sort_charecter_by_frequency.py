"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

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
    for k, v in sorted(hash_map.items(), key= lambda x: x[1], reverse=True):
        res += [k] * v
    return "".join(res)

print(sort_charecters_by_frequency('abbafkkkij'))

def sort_chars_by_freq(s):
    """Use a priority queue"""
    cnt = collections.Counter()

    pq = [(-v,k) for k in cnt.items()]
    heapq.heapify(pq)

    res= []
    while heap:
        v, k = heapq.heappop(pq)
        res += [k] * -v
    return ''.join(res)
