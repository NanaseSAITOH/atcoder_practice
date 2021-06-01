import bisect
def binari_search(left, right):
    OK = False
    mid = 0
    while(right-left > 1):
        mid = (right+left)//2
        flag = 0
        for i in range(N):
            flag += bisect.bisect_left(item[i], mid)+1
        if(flag<=N*(N-1)+1):
            OK = True
        if(OK):
            left = mid
        else:
            right = mid
    return mid
N = int(input())
B = []
A = []
for n in range(N):
    b, a = map(int, input().split())
    B.append(b)
    A.append(a)
item = [[0]*N for i in range(N)]

for i in range(N):
    for n in range(N):
        item[i][n] = B[i]+n*A[i]
max_min = []
for i in range(N):
    max_min.append(item[i][N-1])
left = min(max_min)-1
right = max(max_min)
print(binari_search(left,right))
