# 재귀호출 공부
def solution(a):
    if a <= 20:
        print(a)
        a = a+1
        solution(a)
        

solution(1)