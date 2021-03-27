N, W = map(int, input().split())
vw = [map(int, input().split()) for _ in range(N)]
v, w = [list(i) for i in zip(*vw)]
MAX_V = max(v)
print(N * MAX_V + 1)
dp = [[float("inf")] * (N * MAX_V + 1) for _ in range(N + 1)]
dp[0][0] = 0

print("OK")

for i in range(N):
    for j in range(N * MAX_V + 1):
        if (j < v[i]):
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j - v[i]] + w[i])
            
for i in range(N * MAX_V + 1):
    if (dp[N][i] <= W): ans = i
print(ans)
