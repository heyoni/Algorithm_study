# 프로그래머스
# 시저 암호


# 예전풀이
# a = 'abcdefghijklmnopqrstuvwxyz'
# b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def solution(s, n):
#     answer = ''
#     for i in s:
#         if i in a:
#             answer = answer + a[(a.index(i)+n)%len(a)]
#         elif i in b:
#             answer = answer + b[(b.index(i)+n)%len(b)]
#         else:
#             answer = answer + i
#     return answer


def solution(s, n):
    answer = ''
    for i in s:
        if i != ' ':
            if i.isupper():
                answer += chr((int(ord(i))-65 + n)% 26 + 65)
            else:
                answer += chr((int(ord(i))-97 + n)% 26 + 97)
        else:
            answer += ' '
    return answer