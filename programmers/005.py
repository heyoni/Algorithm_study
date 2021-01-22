# 프로그래머스
# k번째 수

def solution(array, commands):
    answer = []
    for i in commands:
        k = array[(i[0]-1):(i[1])]
        k.sort()
        answer.append(k[(i[2]-1)])
    return answer


a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# [5, 6, 3]

print(solution(a,c))