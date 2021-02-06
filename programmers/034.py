# 프로그래머스
# 키패드 누르기(다시)

def solution(numbers, hand):
    Ltemp = 10
    Rtemp = 12
    answer = ''
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
            Ltemp = n
        elif n in [3,6,9]:
            answer += 'R'
            Rtemp = n
        else:
            L_loc = cal_loc(Ltemp, n)
            R_loc = cal_loc(Rtemp, n)
            if L_loc == R_loc:
                if hand == 'right':
                    answer += 'R'
                    Rtemp = n
                else:
                    answer += 'L'
                    Ltemp = n
            elif L_loc > R_loc:
                answer += 'R'
                Rtemp = n
            else:
                answer += 'L'
                Ltemp = n
    return answer
def cal_loc(temp, n):
    loc = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        10:(3,0),0:(3,1),12:(3,2)
    }
    x_temp, y_temp = loc[temp]
    x_n, y_n = loc[n]

    return abs(x_temp-x_n) + abs(y_temp-y_n)

