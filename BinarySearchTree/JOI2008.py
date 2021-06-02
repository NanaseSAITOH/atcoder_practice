import bisect

d = int(input())
n = int(input())
m = int(input())
store = sorted(list(int(input()) for _ in range(n-1))+[0, d])
client = [int(input()) for _ in range(m)]
ans = 0
for i in client:
    pos = bisect.bisect_left(store, i)
    ans += min(i-store[pos-1], store[pos]-i)
print(ans)
