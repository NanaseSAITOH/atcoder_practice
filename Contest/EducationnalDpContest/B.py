import numpy as np

N, K = map(int, input().split())
H = list(map(int, input().split()))
dp = np.full(N + K, 10 ** 10, dtype=np.int64)
dp[0] = 0
for i in range(1, N):
    for j in range(max(0, i-K), i):
        dp[i] = np.minimum(dp[i],np.abs(H[i] - H[j]) + dp[j])
print(dp[N - 1])
