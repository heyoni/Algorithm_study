# 재귀호출 공부
def solution(a):
    if a > 0:
        print(a)
        a -= 1
        solution(a)

solution(10)