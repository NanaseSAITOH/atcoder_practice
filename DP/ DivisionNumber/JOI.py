N, M, S = map(int, input().split())
L = N * N
dp = [[0] * (M + 1) for _ in range(L + 1)]
dp[0][0]=1
for i in range(1,L+1):
    for j in range(M+1):
        if (j - i) < 0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i][j - i] + dp[i - 1][j]
print(dp[L][M])

