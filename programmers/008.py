# 프로그래머스
# 가운데 글자 가져오기


def solution(s):
    if len(s) % 2 == 0:
        #짝수
        return s[len(s)//2-1:len(s)//2+1]
    else:
        #홀수
        return s[len(s)//2]

