N = list(map(int, input().split()))
N.sort()
ans = N[-1]+N[-2]
print(ans)