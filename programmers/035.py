# 프로그래머스
# 하샤드 수

# def solution(n):
#     x = [int(x) for x in str(n)]
#     if n % sum(x) == 0:
#         return 'true'
#     else:
#         return 'false'


def solution(n):
    return n % sum([int(x) for x in str(n)]) == 0