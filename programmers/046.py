import queue, math


p = [96, 99, 98, 97]
s = [1,1,1,1]
def solution(p, s):
    q = queue.Queue()
    answer = []
    length = len(p)

    # 계산하기 - 며칠 째에 배포가 가능한지?
    t = [(math.ceil(((100-p[i])/s[i]))) for i in range(length)]
    print(t)

    # 큐를 이용하여
    # 1. 이전 리스트 값보다 크면 큐 길이를 세주고, 큐 초기화
    # 2. 이전 리스트 값보다 작으면 큐에 붙여줌
    temp = t[0]
    for i in range(1, length):
        # 앞 원소가 작은 경우 : 큐에다 붙여줌
        if temp >= t[i]:
            q.put(t[i])
        else:
        # 뒤 원소가 큰 경우
            q.put(t[i])
            answer.append(q.qsize())
            q.queue.clear()
            temp = t[i]


    if q.qsize() != 0:
        q.put(t[i])
        answer.append(q.qsize())
    else:
        answer.append(1)

    return answer

print(solution(p, s))