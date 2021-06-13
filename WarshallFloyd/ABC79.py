def warshall_floyd(c):
    for k in range(10):
        for s in range(10):
            for g in range(10):
                c[s][g] = min(c[s][g], c[s][k]+c[k][g])
    return c
H, W = map(int, input().split())
c = [[]*10 for i in range(10)]
for i in range(10):
    c[i] = list(map(int, input().split()))
c = warshall_floyd(c)
chizu = list(range(H))
ans = 0

for i in range(H):
    chizu[i] = list(map(int, input().split()))
for i in range(H):
    for j in range(W):
        if(chizu[i][j] != -1):
            ans += c[chizu[i][j]][1]
print(ans)
