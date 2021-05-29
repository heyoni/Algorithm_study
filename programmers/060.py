# 오픈채팅방

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
user = {}
answer = []

for i in record:
    k = i.split(' ')
    if k[0] == 'Enter':
        user[k[1]] = k[2]
        answer.append([k[1],'님이 들어왔습니다.'])

    elif k[0] == 'Leave':
        answer.append([k[1],'님이 나갔습니다.'])

    elif k[0] == 'Change':
        user[k[1]] = k[2] 

answer = [user[i[0]] + i[1] for i in answer]
