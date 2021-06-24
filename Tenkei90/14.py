from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(-1)
A.sort(reverse=True)
B.sort()
ans = 0
for a in A:
    i = bisect_left(B, a)
    if(i==len(B)):
        ans += abs(B.pop(i)-a)
        B[i]=-1
    else:
        ans += abs(B.pop(i-1)-a)
print(ans)