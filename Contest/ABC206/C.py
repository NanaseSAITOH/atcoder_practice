import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
A = list(map(int,input().split()))
dp = {0:0}
for i in range(len(A)):
    if(A[i] in dp):
        dp[A[i]] = dp[A[i]]+1
    else:
        dp[A[i]] = 1
ans = 0
for v in dp.values():
    if(v==0 or v==1):
        continue
    else:
        ans += comb(v,2)
if(N==1):
    print(1)
else:
    print(comb(N, 2)-ans)
