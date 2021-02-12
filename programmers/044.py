# 프로그래머스
# 주식가격

prices = [1,2,3,2,3,1]
def solution(prices):
    answer = []
    temp = 0

    for i in range(len(prices)-1):
        temp = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                temp += 1
            else:
                temp +=1
                break

        answer.append(temp)
    answer.append(0)
    return answer
print(solution(prices))