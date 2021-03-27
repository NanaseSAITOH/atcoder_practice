N, W = map(int, input().split())
vw = [map(int, input().split()) for i in range(N)]
v, w = [list(i) for i in zip(*vw)]
dp = [[0]*(W+1) for i in range(N+1)]
for i in range(N):
    for j in range(W + 1):
        if (j < w[i]):
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i + 1][j - w[i]] + v[i], dp[i][j])
            
print(dp[N][W])
