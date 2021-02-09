# 프로그래머스
# 비밀지도

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
n = 6
answer=[]


def cal(n,a1,a2):
    temp = bin(a1|a2)[2:]
    return str(temp).zfill(n)

def solution(n, arr1, arr2):
    for i in range(n):
        answer.append(cal(n,arr1[i],arr2[i]).replace('0',' ').replace('1','#'))

    return answer

print(solution(n,arr1,arr2))