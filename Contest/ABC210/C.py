from heapq import heappush, heappop
N, K = map(int, input().split())
a = list(map(int, input().split()))
hq = []
for i,v in enumerate(a):
    heappush(hq, (v,i))
ans = list(range(N))
okasi_num = K//N
okasi_amari = K%N
for n in range(N):
    id = heappop(hq)[1]
    if(n<=(K%N-1)):
        ans[id] = okasi_num+1
    else:
        ans[id] = okasi_num
for a in ans:
    print(a)
