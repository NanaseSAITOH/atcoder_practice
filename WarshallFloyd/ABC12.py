def warshall_floyd(N,c):
    for k in range(N):
        for s in range(N):
            for g in range(N):
                c[s][g] = min(c[s][g], c[s][k]+c[k][g])
    return c

N, M = map(int,input().split())
c = [[float("inf")]*N for _ in range(N)]
for m in range(M):
    s, g, t = map(int,input().split())
    s-=1
    g-=1
    c[s][g] = t
    c[g][s] = t
for v in range(N):
    c[v][v] = 0
ans = warshall_floyd(N, c)
most_big = 10**10
for i in range(N):
    if(most_big>max(ans[i])):
        most_big = max(ans[i])
print(most_big)
