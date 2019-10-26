# Пересечение множеств
set1 = set(map(int, set(input().split())))
set2 = set(map(int, set(input().split())))
result = sorted(list(set1 & set2))
for i in result:
    print(i, end=" ")
