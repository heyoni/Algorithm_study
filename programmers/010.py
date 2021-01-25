# 프로그래머스
# 나누어 떨어지는 숫자 배열


def solution(arr, divisor):
    answer =[]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer


# a.sort() : 그 자리에서 정렬하고 목록인덱스 변경
# sorted(a) : 새로운 리스트를 만들고 원래 리스트는 그대로 유지

print(solution([5, 9, 7, 10],5))