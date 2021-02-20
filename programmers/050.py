a = []
n = 4
k = 0
for i in range(1,n+1):
    for j in range(i):
        # 배열의 첫번째 원소는 무조건 1번째 1, 2번째 2, ...
        if j == 0:
            temp = [i]
        
        # 마지막 줄인 경우(ex. 5,6,7,8,9)
        elif i == n:
            temp += [i+j]
            k = i+j
        # 그 외의 경우

    a.append(temp)

# def direction(k):
#     if k == 0:
#         x += 1
#     elif k == 1:
#         y += 1
#     else:
#         x -= 1
#         y -= 1

#     return x, y




