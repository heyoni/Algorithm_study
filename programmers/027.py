# 프로그래머스
# 정수 제곱근 판별

import math

def solution(n):
    n = math.sqrt(n)
    if n == int(n):
        return int((n+1)**2)
    else:
        return -1
