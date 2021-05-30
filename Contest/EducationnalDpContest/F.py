s = input()
t = input()
dp = [[0]*(len(s)) for i in range((len(t)))]
for i in range(len(t)):
    for j in range(len(s)):
        dp[i][j] = max(dp[i-1][j] + (t[i] == s[j]), dp[i][j-1])
n,m = len(s), len(t)
ans = ""
while n >= 0 and m >= 0:
    if dp[m-1][n-1] == dp[m-1][n-2]:
        m -= 1
    elif dp[m-1][n-1] == dp[m-2][n-1]:
        n -= 1
    else:
        ans = s[n-1]+ans
        n -= 1
        m -= 1
print(ans)
