stages = [4,4,4,4,4]
n = 4
stages_length = len(stages)
failure_rate = []
answer = []

for i in range(1,n+1):
    failure_rate.append(stages.count(i)/stages_length)
    stages_length -= stages.count(i)

for j in range(n):
    answer.append(failure_rate.index(max(failure_rate))+1)
    failure_rate[failure_rate.index(max(failure_rate))] = -1

print(answer)