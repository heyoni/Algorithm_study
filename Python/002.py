# 숫자 입력받고 최솟값 구하기

n = int(input('n을 입력해주세요 : '))
l = []
for i in range(n):
    l.append(int(input('숫자를 입력해주세요 : ')))

answer = 999
for j in l:
    if j < answer:
        answer = j
    
print(answer)