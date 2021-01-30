# 프로그래머스
# 소수찾기

def solution(n):
    count = 0
    primes = []
    a = [False, False] + [True] *(n-1)
    for i in range(2, n+1):
        if a[i] == True:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return len(primes)