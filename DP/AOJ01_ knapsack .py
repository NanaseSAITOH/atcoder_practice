N, W = map(int, input().split())
vw = [map(int, input().split()) for n in range(N)]
v, w = [list(i) for i in zip(*vw)]
dp = [[0] * (W + 1) for i in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(W+1):
        if j < w[i]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
            
print(dp[0][W])
