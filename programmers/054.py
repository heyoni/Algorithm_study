def solution(p):
    if p =='':
        return p
    
    u, v = devide_uv(p)
    if right(u):
        return u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        temp = u[1:-1]
        for i in temp:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer

def right(s):
    stack = []
    for i in s:
        if i == ')':
            if stack:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True
            


def devide_uv(s):
    count_l = 0
    count_r = 0
    temp = ''
    for i in range(len(s)):
        if s[i] == '(':
            count_l += 1
        else:
            count_r += 1
        if count_l == count_r:
            return s[:i+1], s[i+1:]
