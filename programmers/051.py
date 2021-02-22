# 프로그래머스
# 문자열 압축


s = "a"
def solution(s):
    temp_list = []
    STR, COUNT = 0, 1

    if len(s) == 1:
        return 1
    else:
        # 1. 쪼개기
        for i in range(1, len(s)):
            compressed = ''
            temp = [s[j:j+i] for j in range(0, len(s), i)]
            stack = [[temp[0], 1]]
            
            for k in temp[1:]:
                # 2-1. 앞 문자와 같다면 count+=1
                if stack[-1][STR] != k:
                    stack.append([k, 1])
            
                # 2-2. 앞 문자와 다르다면 count 초기화
                else:
                    stack[-1][COUNT] += 1
            compressed += ('').join([str(cnt) + w if cnt > 1 else w for w, cnt in stack])
            temp_list.append(len(compressed))
        return min(temp_list)

print(solution(s))