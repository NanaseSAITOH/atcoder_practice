N = int(input())
a = []
b = []
c = []
for i in range(N):
    A, B, C = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)
dp = [[0]*3 for i in range(N)]

dp[0][0] = a[0]
dp[0][1] = b[0]
dp[0][2] = c[0]

for i in range(1,N,1):
    dp[i][0] = max(a[i]+dp[i-1][1], a[i]+dp[i-1][2])
    dp[i][1] = max(b[i]+dp[i-1][0], b[i]+dp[i-1][2])
    dp[i][2] = max(c[i]+dp[i-1][1], c[i]+dp[i-1][0])
print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2]))
