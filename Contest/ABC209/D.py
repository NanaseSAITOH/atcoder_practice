N = int(input())
T = list(map(int, input().split()))
sum = sum(T)

#dp[i][j]:アイテムiまででjを作れるか？
dp = [[False]*(sum+1) for _ in range(N+1)]

dp[0][0]=True
for i in range(N):
    t = T[i]
    for j in range(sum + 1):
        if dp[i][j]:
            dp[i + 1][j] = True
        if j - t >= 0 and dp[i][j - t]:
            dp[i + 1][j] = True

ans = 10 ** 10
for i in range(sum + 1):
    if dp[N][i]:
        score = max(i, sum - i)  # 片方をiにすると、もう片方はS-iになります
        ans = min(ans, score)
print(ans)


'''これはなぜか通らない
for s in range(sum//2+1,sum+1,1):
    if(dp[-1][s]):
        print(s)
        break;
'''
