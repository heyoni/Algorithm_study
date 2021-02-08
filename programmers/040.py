# from itertools import combinations

# def solution(d, budget):
#     if sum(d) <= budget:
#         return len(d)
#     else:
#         for j in range(len(d),1,-1):
#             l = list(combinations(d, j))
#             for i in range(len(l)):
#                 if sum(l[i]) <= budget:
#                     return len(l[i])
#         if budget in d:
#             return 1
#         else:    
#             return 0

def solution(d, budget):
    d.sort()
    answer = 0
    sum = 0
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1
        else:
            break
    return answer