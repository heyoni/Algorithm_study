import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while True:
        min_food1 = heapq.heappop(scoville)
        if min_food1 >= K:
            return answer
        elif len(scoville) == 0:
            return -1
        min_food2 = heapq.heappop(scoville)

        temp = min_food1 + (min_food2 * 2)
        heapq.heappush(scoville,temp)
        answer += 1