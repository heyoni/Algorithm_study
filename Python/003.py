# 동명이인
# n명의 사람 중 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘

l = ['jacob','tom','arex','tom']

l.sort()

answer = set()
for i in range(0, len(l)-1):
    if l[i] == l[i+1]:
        answer.add(l[i])
print(answer)