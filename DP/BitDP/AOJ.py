V, E = map(int, input().split())
path = [[float("inf")]*V for i in range(V)]
for e in range(E):
    s, g, d = map(int, input().split())
    path[s][g] = d

dp = [[float("inf")]*(1<<V) for i in range(V)]

dp[0][(1 << V)-1] = 0

for S in range((1 << V)-2, -1, -1):
    for v in range(V):
        for u in range(V):
            if(not((S >> u) & 1)):
                dp[v][S] = min(dp[v][S], dp[u][S | 1 << u]+path[v][u])
if(dp[0][0]==float("inf")):
    print(-1)
else:print(dp[0][0])
