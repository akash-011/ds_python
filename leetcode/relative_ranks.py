from re import S


"""
https://leetcode.com/problems/relative-ranks/description/
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.

"""

def relative_ranks(score):
    medal = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
    answer = [""] * len(score)
    print(answer)
    score_map = {}

    for i in range(len(score)):
        score_map[score[i]] = i
    print(score_map)

    score.sort(reverse=True)

    for i in range(len(score)):
        if i < 3:
            answer[score_map[score[i]]] = medal[i]
        else:
            answer[score_map[score[i]]] = str(i+1)
    return answer

print(relative_ranks([5,1,3,4,2]))