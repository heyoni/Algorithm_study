# 프로그래머스
# 삼각달팽이


import itertools
def direction(x,y,k):
    if k % 3 == 0:
        x += 1
    elif k % 3 == 1:
        y += 1
    else:
        x -= 1
        y -= 1

    return x, y

def solution(n):
    idx = 1
    x, y = -1, 0
    answer = [[0 for j in range(i)] for i in range(1,n+1)]
    for i in range(n):
        for j in range(i,n):
            x, y = direction(x, y, i)
            print(x,y)
            answer[x][y] = idx
            idx += 1
    return list(itertools.chain.from_iterable(answer))



print(solution(4))
