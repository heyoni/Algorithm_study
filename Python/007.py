# 3과 5의 배수 계산하기

def solution(n):
    if (n % 3 == 0) and (n % 5 == 0):
        print('3과 5의 배수')
    else:
        print('아님')

solution(15)