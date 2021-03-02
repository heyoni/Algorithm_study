# 프로그래머스
# 가장 큰 수

def solution(numbers):
    k = []
    answer = ''
    numbers = list(map(str, numbers))

    for i in numbers:
        k.append([int((i*4)[:4]),i])

    k.sort(reverse=True)

    for j in k:
        answer += j[1]

    return str(int(answer))