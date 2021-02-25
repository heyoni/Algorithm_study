# 프로그래머스
# 괄호변환 - 올바른 괄호인지 return 해주는 것만 구현함

def solution(p):
    stack = []
    for i in p:
        if i == ')':
            if stack:
                # 스택에 값이 있다면 앞부분은 무조건 '('
                # 그러므로 값을 빼준다
                stack.pop()
            else:
                # 스택에 값이 없다면 올바른 괄호가 아님
                return False
        else:
            stack.append(i)

    return True
