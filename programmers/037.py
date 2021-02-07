# 프로그래머스
# 행렬의 덧셈


def solution(arr1, arr2):
    return ([[x+y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)])