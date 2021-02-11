# 프로그래머스
# 다트게임(실패)

def solution(s):
    t = ''
    d = {'S':'**1','D':'**2','T':'**3'}
    k = 0
    for i in s:
        if i in d:
            t += d[i] +'+'

        else:
            if i == '*':
                if k == 3:
                    if s[-4] == '*' or s[-4] == '#':
                        t = t[:-12] + '' + t[-12:-1] +')*2+'

                    else:
                        t = t[:-10] + '(' + t[-10:-1] +')*2+'

                else:
                    t = '(' + t[:-1] +')*2+'
            elif i == '#':
                t = t[:-1] +'*-1+'
            else:
                t += i
                k += 1
    print(t[:-1])
    return eval(t[:-1])



print(solution(s))