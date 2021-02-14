# 프로그래머스
# 프린터(런타임오류)

def solution(p, location):
    k = [(p[i], i) for i in range(len(p))]
    loc = (p[location],location)
    
    stack,temp = cal(k)
    
    while temp:
        stack2,temp = cal(temp)
        s = stack+stack2

    return s.index(loc)+1

def cal(n):
    t = n[0][0]
    stack = []
    temp = []

    for i in n:
        if t < i[0]:
            # 앞 리스트에 있는 값들을 꺼내줌
            temp = stack.copy()
            stack = []
            stack.append(i)
        else:
            # 리스트에 넣어줌
            stack.append(i)
        t = i[0]
    return stack,temp
