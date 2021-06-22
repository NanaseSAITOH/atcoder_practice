from bisect import bisect_left, bisect_right
N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
ans = []
for i in range(Q):
    youso = int(input())
    left_id = bisect_left(A, youso)
    if(left_id==0):
        print(abs(A[left_id]-youso))
    elif(left_id == N):
        print(abs(A[left_id-1]-youso))
    else:
        print(min(abs(A[left_id-1]-youso), abs(A[left_id]-youso)))
