from bisect import bisect_right


def bonary_search(B, a):
    left = 0
    right = len(B)
    while(left<right):
        mid = (left+right)//2
        if(B[mid]<a):
            left = mid+1
        elif(B[mid]>=a):
            right = mid
    return left


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
B2 = []
for a in A:
    pos = bonary_search(B,a)
    B2+=B[pos:]
ans = 0
for b in B2:
    pos = bonary_search(C, b)
    ans += N-(pos)
print(ans)
