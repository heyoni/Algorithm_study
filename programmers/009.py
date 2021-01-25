# 프로그래머스
# 중복은 싫어

def solution(arr):
    answer = []
    temp = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])

    answer.append(arr.pop())
    return answer