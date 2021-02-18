# 프로그래머스
# 다리를 지나는 트럭


bridge_length = 2
weight = 10
truck_weight = [7,4,5,6]

from collections import deque
def solution(bridge_length, weight, truck_weight):
    total_weight = 0
    answer = 0 # 결과값
    dq = deque(0 for _ in range(bridge_length))

    while truck_weight:
        total_weight -= dq.popleft()
        if total_weight + truck_weight[-1] > weight:
            dq.append(0)

        else:
            truck = truck_weight.pop()
            dq.append(truck)
            total_weight += truck
        answer += 1

    answer += bridge_length
    return answer
print(answer)