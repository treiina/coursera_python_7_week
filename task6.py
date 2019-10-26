# Полиглоты
N = int(input())
info = []
for i in range(N):
    num_Mi = int(input())
    info.append(set())
    for j in range(num_Mi):
        info[i].add(input())
result1, result2 = set(info[0]), set()
for i in info:
    result1 &= i
print(len(result1))
for i in sorted(list(result1)):
    print(i)

for i in info:
    result2 |= i
print(len(result2))
for i in sorted(list(result2)):
    print(i)
