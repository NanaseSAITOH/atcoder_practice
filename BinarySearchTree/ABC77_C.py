from bisect import bisect_right


def bonary_search(B, a):
    left = -1
    right = N
    while(left<right):
        mid = (left+right)//2+1
        last = mid
        if(B[mid]<a):
            left = mid+1
            last = left
        elif(B[mid]>a):
            right = mid-1
            last =right
        else:
            return mid
    return last


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
    B2+=B[pos+1:]
ans = 0
for b in B2:
    pos = bonary_search(C, b)
    ans += N-(pos+1)
print(ans)
