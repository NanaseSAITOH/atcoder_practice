N = int(input())
S = list(input())
atcoder = list("atcoder")
dp = [[0]*N for i in range(len(atcoder))]
for ac in range(len(atcoder)):
    last = 1
    for n in range(N):
        if(atcoder[ac] == S[n]):
            if (ac == 0 and n == 0):
                dp[ac][n] = 1
            elif(ac == 0 and dp[ac][n-1] == 0):
                dp[ac][n] = 1
            elif(ac == 0):
                dp[ac][n] = dp[ac][n-1]+1
            else:
                dp[ac][n] = dp[ac-1][n]+dp[ac][n-1]
                if(dp[ac][n] != 0):
                    last += 1
        else:
            if(n == 0):
                dp[ac][n] = 0
            else:
                dp[ac][n] = dp[ac][n-1]
print(dp[-1][-1] % (10**9+7))
