import heapq
import sys

L, P, N = map(int, input().split())
A = [i for i in map(int, input().split())]
B = [i for i in map(int, input().split())]
pque = []

A += [L]
B += [0]
N += 1

gass = P
pos = 0
ans = 0

for i in range(N):
    d = A[i] - pos
    while gass - d < 0:
        if len(pque) == 0:
            print("-1")
            sys.exit()
            
        gass += -1 * heapq.heappop(pque)
        ans += 1
    gass = gass - d
    pos = A[i]
    heapq.heappush(pque, -1 * B[i])

print(ans)

