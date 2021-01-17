# 프로그래머스
# 체육복

def solution(n, lost, reverse):
    temp = []
    answer = n - len(lost)
    # 도난당한 학생이 여벌옷을 가지고 있을 경우
    for i in lost:
        if i in reverse:
            reverse.remove(i)
            temp.append(i)
            answer += 1            
    # 그 외의 경우
    for i in lost: 
        # temp에 있는 값은 위에서 도난당한 학생이 여벌옷을 갖고 있는 경우
        # for문을 실행하지 않고 그냥 지나감
        if i in temp:
            continue
        # reverse가 0일 경우 모든 경우를 계산 한 결과이므로 return해줌
        if len(reverse) == 0:
            return answer
        else:
            if i-1 in reverse:
                answer += 1
                reverse.remove(i-1)
            elif i+1 in reverse:
                answer += 1
                reverse.remove(i+1)
    return answer