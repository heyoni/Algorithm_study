# 프로그래머스
# 문자열 압축 2 (실패)

s = 'aabbaccc'
stack = []
answer = []
temp = ''


for i in range(1, len(s)):
    l = [s[j:j+i] for j in range(0,len(s),i)]
    for j in range(len(l)-1):
        # 앞에 값과 같다면
        if l[j] == l[j+1]:
            # 스택에 넣어줌
            stack.append(l[j])
            continue


        # 앞에 값과 다르다면
        else:
            # 스택에 값이 있다 = 현재 값과 앞에 값이 일치한다 = 스택에 넣어줘야 한다.
            if len(stack) != 0:
                # 현재값을 다시 append 해줌
                stack.append(l[j])
                # 길이 구하고
                k = len(stack)
                # 새 배열에 값을 넣고(2a2ba3c)
                temp += (str(k)+stack[0])
                # 다 빼줌
                stack.clear()

            # 스택에 값이 없고 다르다
            else:
                temp += (l[j])

            continue
    if stack:
        # 스택에 값이 남아있다
        stack.append(l[j])
        # 길이 구하고
        k = len(stack)
        # 새 배열에 값을 넣고(2a2ba3c)
        temp += (str(k)+stack[0])
        # 다 빼줌
        stack.clear()
        print(temp)
    else:
        temp += l[j+1]
    answer.append(temp)
    temp = ''
    print(answer)
    