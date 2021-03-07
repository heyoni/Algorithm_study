# 짝 만들기

l=['tom','jerry','mike']

for i in range(len(l)):
    for j in range(i+1,len(l)):
        print(l[i],l[j])