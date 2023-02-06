"""
https://leetcode.com/problems/plus-one/description/

"""

def solution(digits):
    final_answer = int(''.join(map(str, digits))) + 1
    res = [int(x) for x in str(final_answer)]
    return res 

