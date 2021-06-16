N, Q = map(int, input().split())
A = list(map(int, input().split()))
K = list(range(Q))
for q in range(Q):
    K[q]=int(input())
dp = []
dp.append(A[0]-1)
for i in range(1,N):
    dp.append(dp[i-1]+A[i]-A[i-1]-1)
for i in range(1,Q):
    if(dp[-1]<K[i]):
        ans = A[-1]+K[i]-dp[-1]
        print(ans)
    else:
        