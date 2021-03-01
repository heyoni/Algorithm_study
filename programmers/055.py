from itertools import combinations

# def solution(number, k):
#     number = list(map(str, number))
#     l = set(combinations(number, len(number)-k))

#     t = []
#     temp = ''
#     for i in l:
#         for j in i:
#             temp += j
#         t.append(int(temp))
#         temp = ''
#     return str(max(t))


# def solution(number, k):
#     number = list(map(str, number))
#     l = set(combinations(number, len(number)-k))
#     t = []
#     for i in l:
#         t.append(''.join(i))
#     return str(max(t))


def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while len(stack) > 0 and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack) 
print(solution('4177252841', 4))



