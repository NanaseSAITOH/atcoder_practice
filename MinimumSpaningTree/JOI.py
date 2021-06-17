from heapq import heappush, heappop
import numpy as np

N, M, K = map(int, input().split())
C = [[] for i in range(N)]
screen = [False]*N

for i in range(M):
    s, g, d = map(int, input().split())
    C[s-1].append([g-1, d])
    C[g-1].append([s-1, d])
hq = []
for g,d in C[0]:
    heappush(hq,(d, g))
ans = 0
screen[0] = True
load_cost = []
while hq:
    cost, goal = heappop(hq)
    ans += cost
    load_cost.append(cost)
    if(screen[goal]==True):
        continue
    screen[goal] = True
    for g,d in C[goal]:
        if(screen[g]==False):
            heappush(hq,(d,g))

for k in range(K-1):
    ans-=load_cost[k]
print(ans)
