s = list(input())
N = len(s)
ATCG = ["A", "T", "C", "G"]
dp = [0]*(N+1)
for i in range(1, N+1, 1):
    if(s[i-1] in ATCG):
        dp[i]=dp[i-1]+1
print(max(dp))
