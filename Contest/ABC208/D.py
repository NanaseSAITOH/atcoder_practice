N, K = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
mean = int(K**2/2)+1
dp = [[[] for j in range(N-K+1)] for i in range(N-K+1)]
ans = []
for ki in range(K):
    for kj in range(K):
        dp[0][0].append(A[ki][kj])
last_i=0
last_j=0
for i in range(N-K+1):
    for j in range(N-K+1):
        if(i==0 and j==0):continue
        if(last_i!=i):
            dp[i][j] = dp[last_i][j]
            for k in range(K):
                dp[i][j].append(A[i+k][j])
                dp[i][j].remove(A[i-k][j])
        elif(last_j!=j):
            dp[i][j] = dp[i][last_j]
            for k in range(K):
                dp[i][j].append(A[i][j+k])
                dp[i][j].remove(A[i][j-k])
        dp[i][j] = sorted(dp[i][j], reverse=True)
        ans.append(dp[i][j][mean-1])
        last_j = j
        last_i = i
print(min(ans))
