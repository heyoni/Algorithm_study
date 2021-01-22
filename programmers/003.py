# 프로그래머스
# 모의고사

def solution(answer):
    A = [1, 2, 3, 4, 5]    
    B = [2, 1, 2, 3, 2, 4, 2, 5]
    C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_count = [0, 0, 0]
    answer_count[0] = counter(answer, A)
    answer_count[1] = counter(answer, B)
    answer_count[2] = counter(answer, C)

    m = max(answer_count)
    k = [(i+1) for i in range(len(answer_count)) if answer_count[i] == m]
    


def counter(answers, supo):
    value = 0
    supo_len = len(supo)
    for i in range(len(answers)):
        if answers[i] == supo[i % supo_len]:
            value += 1
    return value