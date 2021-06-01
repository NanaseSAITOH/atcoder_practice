from bisect import bisect_right


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
B2 = []
for a in A:
    pos = bisect_right(B, a)
    B2+=B[pos:]
ans = 0
for b in B2:
    pos = bisect_right(C, b)
    ans += N-pos
print(ans)
