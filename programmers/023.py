# 프로그래머스
# 이상한 문자 만들기
# TrY

def solution(s):
    answer = ''
    k = 0
    for i in s:
        if i.isalpha():
            if k % 2 == 0:
                answer += i.upper()
                k+=1
            else:
                answer += i.lower()
                k+=1
        else:
            answer += i
            k = 0
    return answer
