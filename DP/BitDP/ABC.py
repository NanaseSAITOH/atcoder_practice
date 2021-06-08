# https://atcoder.jp/contests/s8pc-1/submissions/23196687
N, M = map(int, input().split())
Distance = [[float("inf") for _ in range(N)] for _ in range(N)]
Time = [[0 for _ in range(N)] for _ in range(N)]
for m in range(M):
    s, g, d, time = map(int, input().split())
    Distance[s-1][g-1] = d
    Distance[g-1][s-1] = d
    Time[s-1][g-1] = time
    Time[g-1][s-1] = time

dp_time = [[float("inf")]*N for i in range((1 << N))]
dp_load_num = [[0]*N for i in range((1 << N))]

dp_time[0][0] = 0
dp_load_num[0][0] = 1

for S in range((1 << N)):
    for v in range(N):
        for u in range(N):
            #Sにvが存在するとき
            if(not(S & 1 << v == 0)):
                a = bin(S)
                b = bin(1 << v)
                #排他的論理和(Sとvの一致箇所を除去する)(Sからvを除去する)
                c = bin(S ^ (1 << v))
                if(dp_time[S][v] > Distance[v][u]+dp_time[S ^ (1 << v)][u]
                   and Time[v][u] >= Distance[v][u]+dp_time[S ^ (1 << v)][u]):
                    dp_time[S][v] = Distance[v][u]+dp_time[S ^ (1 << v)][u]
                    dp_load_num[S][v] = dp_load_num[S ^ (1 << v)][u]

                elif(dp_time[S][v] == Distance[v][u]+dp_time[S ^ (1 << v)][u] and Time[v][u] >= Distance[v][u]+dp_time[S ^ (1 << v)][u]):
                    dp_load_num[S][v] += dp_load_num[S ^ (1 << v)][u]

if(dp_load_num[-1][0] == 0):
    print("IMPOSSIBLE")
else:
    print(dp_time[-1][0], dp_load_num[-1][0])
 
