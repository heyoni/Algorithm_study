from itertools import combinations

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

# 딕셔너리(해시) 만들기
d_clothes = dict(clothes)
temp = []
answer = len(clothes)

for i in range(2, len(d_clothes)+1):
    temp.append(list(combinations(d_clothes, i)))
print(temp)

# value 값을 가지고 경우의 수 만들기
# for i in d_clothes:
    # if d_clothes
# 같으면 추가할 수 없고
# 다르면 추가할 수 있음