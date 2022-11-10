from re import S


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