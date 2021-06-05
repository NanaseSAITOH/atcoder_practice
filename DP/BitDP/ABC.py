N, M = map(int, input().split())
D = [[float("inf")]*N for i in range(N)]
Time = [[float("inf")]*N for i in range(N)]
for m in range(M):
    s, g, d, time = map(int, input().split())
    D[s-1][g-1] = d
    Time[s-1][g-1] = time

dp_time = [[0]*(1 << N) for i in range(N)]
dp_load_num = [[0]*(1 << N) for i in range(N)]

dp_time[0][(1 << N)-1] = float("inf")
dp_load_num[0][(1 << N)-1] = 0

for S in range((1 << N)-2, -1, -1):
    for v in range(N):
        for u in range(N):
            if(not((S >> u) & 1)):
                if(Time[v][u] > D[v][u]+dp_time[u][S | 1 << u]):
                    dp_time[v][S] = D[v][u]+dp_time[u][S | 1 << u]
                    dp_load_num[v][S] += dp_load_num[u][S | 1 << u]+1
print(dp_time[0][0])
print(dp_load_num[0][0])
