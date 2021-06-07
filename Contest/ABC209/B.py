N = int(input())
A = list(map(int, input().split()))
ans = 0
for n in range(N):
    if(A[n]>10):
        ans+=(A[n]-10)
print(ans)