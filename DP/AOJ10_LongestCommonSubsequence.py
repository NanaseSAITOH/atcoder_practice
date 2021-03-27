N = int(input())

c = [input() for h in range(N*2)]

for n in range(N):
    s = c[2*n]
    t = c[2 * n + 1]
    dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
    a = len(s)
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                
    print(dp[len(s)][len(t)])
