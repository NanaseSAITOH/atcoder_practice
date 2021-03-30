N, M = map(int, input().split())
A = [i for i in map(int, input().split())]
B = [i for i in map(int, input().split())]
sum_A = 0
sum_B = 0
for i in A:
    sum_A = sum_A + i
for i in B:
    sum_B = sum_B + i
    
def dp_a():
    dp = [[0] * (sum_A + 1) for i in range(M + 1)]
    dp[0][0]=1
    for i in range(1,M+1):
        for j in range(sum_A + 1):
            if (j - i < 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - i] + dp[i - 1][j]
    return dp[M][sum_A]

def dp_b():
    dp = [[0] * (sum_B + 1) for i in range(N + 1)]
    dp[0][0] = 1
    for i in range(1,N+1):
        for j in range(sum_B+1):
            if (j - i < 0):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - i] + dp[i - 1][j]
    return dp[N][sum_B]

print(dp_a())
print(dp_b())
