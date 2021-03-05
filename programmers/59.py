from itertools import combinations

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

d_clothes = dict()
answer = 1

for name, kind in clothes:
    if kind in d_clothes:
        d_clothes[kind] += 1

    else:
        d_clothes[kind] = 1

for i in d_clothes.values():
    answer *= (i + 1)

print(answer)