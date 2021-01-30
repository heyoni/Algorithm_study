# 프로그래머스
# 수박수박수박수박수박수?

def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer

# 다른사람의 답안
def solution2(n):
    s = '수박' * n
    return s[:n]
