def calculate_all_sum(mid):
    for i in range(N):
        for j in range(N):
            all_sum[i+1][j+1] = (A[i][j]>mid)
    #横方向の累積和
    for i in range(N+1):
        for j in range(N):
            all_sum[i][j+1] += all_sum[i][j]
    #縦方向の累積和
    for i in range(N):
        for j in range(N+1):
            all_sum[i+1][j] += all_sum[i][j]
    return all_sum

N, K = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
mean = int(K**2/2)+1

all_sum = [[0]*(N+1) for i in range(N+1)]

left = -1
right = float("inf")
while(1<left-right):
    mid = (left+right)/2
    OK = False
    all_sum=calculate_all_sum(mid)
    for i in range(N-K+1):
        for j in range(N-K+1):
            now = all_sum[i+K][j+K]
            now -= all_sum[i+K][j]
            now -= all_sum[i][j+K]
            now += all_sum[i][j]
            if(now<mean):
                OK=True
    if(OK):
        left = mid
    else:
        right=mid
print(right)
