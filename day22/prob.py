n = 3
trust = [[1, 3], [2, 3], [3, 1]]

dic = {}

for i in range(1, n + 1):
    if i not in dic:
        dic[i] = []

for i in trust:
    dic[i[0]].append(i[1])

degree = {}

for i in dic.keys():
    if i not in degree:
        degree[i] = [len(dic[i]), 0]

for u, v in trust:
    degree[v][1] += 1

for i, j in degree.items():
    if j[0] == 0 and j[1] == n - 1:
        print(i)
        break
else:
    print("-1")