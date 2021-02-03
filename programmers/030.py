# 프로그래머스
# 키패드 누르기

def solution(numbers, hand):
    answer = ''
    Ltemp = 10
    Rtemp = 12

    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            Ltemp = i 

        elif i in [3, 6, 9]:
            answer += 'R'
            Rtemp = i 

        elif i in [2, 5, 8, 0]:
            R = cal_distance(Rtemp, i)
            L = cal_distance(Ltemp, i)
            if R == L:
                answer += hand[0].upper()
                if hand[0].upper() == 'R':
                    Rtemp = i
                else:
                    Ltemp = i
            elif R > L:
                answer += 'L'
                Ltemp = i 
            else:
                answer += 'R'
                Rtemp = i
    return answer


def cal_distance(temp, n):
    location = {1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
                4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
                7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
                10 : (3, 0), 0 : (3, 1), 12 : (3, 2)}
    temp_x, temp_y = location[temp]
    n_x, n_y = location[n]
    return abs(temp_x - n_x) + abs(temp_y - n_y)

