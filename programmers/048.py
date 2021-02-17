# 프로그래머스
# 스킬트리


def solution(skill, skill_trees):
    answer = 0
    t = 0
    for i in skill_trees:
        for j in i:
            if j in skill:
                if skill[t] != j:
                    print(skill[t],j)
                    break
                else:
                    t+=1
            answer += 1
        t=0
        

    return answer


print(solution('CBD',["BACDE", "CBADF", "AECB", "BDA"]))