# 프로그래머스
# 괄호변환 - 올바른 괄호인지 return 해주는 것만 구현함

def solution(p):
    # 1번
    if p == '':
        return ''

    # 2번
    u, v = devide_uv(p)

    # 3번
    if right(u):
        # 3-1번
        return u + solution(v)
    else:
        # 4-1,2,3번
        answer = '('
        answer += solution(v)
        answer += ')'
        
        # 4-4번
        temp_u = u[1:-1]
        for i in temp_u:
            if i == '(':
                answer += ')'
            else:
                answer += '('

        return answer 

# u와 v를 균형잡힌 문자열로 변환하기
# (, )의 갯수가 똑같으면 균형잡힌 문자열이므로 같아지는 때에 u,v로 분리한다.
def devide_uv(s):
    count_i = 0 # ( 의 갯수
    count_j = 0 # ) 의 갯수

    for i in range(len(s)):
        if s[i] == '(':
            count_i+=1
        else:
            count_j+=1
        if count_i == count_j:
            break
    return s[:i+1], s[i+1:]

# 올바른 괄호 문자열인지 판단하기
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

def right2(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return True