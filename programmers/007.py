# 프로그래머스
# 3진법 뒤집기

# def solution(n):
    
#     return answer
answer = 0

n=125
k=''
while n>2:
    k = k+str(n%3)
    n //= 3
        
    print(n, k)

k = str(int(k+str(n)))

t = 0
k = k[::-1]
for i in k:
    answer += int(i)*(3**t)
    t+=1
print('last:',k)
print(answer)