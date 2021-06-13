import sys
V, E = map(int,input().split())
c = [[float("inf")]*V for i in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    c[s][t]=d
for i in range(V):
    c[i][i]=0
for k in range(V):
    for s in range(V):
        for g in range(V):
            c[s][g]=min(c[s][g], c[s][k]+c[k][g])
            if(c[s][s]<0):
                print("NEGATIVE CYCLE")
                sys.exit()
ans= [[""]*V for i in range(V)]
for i in range(V):
    for j in range(V):
        if(c[i][j]==float("inf")):
            ans[i][j]="INF"
        else:
            ans[i][j] = str(c[i][j])
for i in ans:
    print(*i)
