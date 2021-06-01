def binary_search(a, L):
    left = -1
    right = N+1
    while(right-left>1):
        mid = (right+left)//2
        if(L[mid-1]<a):
            left = mid
        elif(L[mid-1] > a):
            right = mid
    if L[mid-1] > a:
      return mid
    else:
      return mid + 1

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
C = sorted(C)
B2 = []
for a in A:
    pos = binary_search(a, B)
    B2+=B[pos:]
ans = 0
for b in B2:
    pos = binary_search(b, C)
    ans += len(C[pos:])
print(ans)
