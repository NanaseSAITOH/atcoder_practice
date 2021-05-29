import sys
sys.setrecursionlimit(100000)

N = int(input())
route = [[] for _ in range(N)]
color = [-1 for _ in range(N)]
for i in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    route[u].append((v, w))
    route[v].append((u, w))

def dfs(n):
    for i in route[n]:
        if (color[i[0]] == -1 and i[1] % 2 == 0):
            color[i[0]] = color[n]
            dfs(i[0])
        elif (color[i[0]] == -1 and i[1] % 2 != 0):
            color[i[0]] = 1^color[n]
            dfs(i[0])

color[0] = 0
dfs(0)

for i in range(N):
    print(color[i])
