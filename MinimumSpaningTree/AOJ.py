from heapq import heappush, heappop

V, E = map(int, input().split())
screen = [False]*V
C = [[] for i in range(V)]
hq = []
for i in range(E):
    s, g, d = map(int, input().split())
    C[s].append([g,d])
    C[g].append([s, d])
for i in C[0]:
    heappush(hq, (i[1], i[0]))
screen[0] = True
ans = 0
while not(all(screen)):
    h = heappop(hq)
    cost = h[0]
    goal = h[1]
    ans += cost
    screen[goal]=True
    for i in C[goal]:
        if(screen[i[0]]==False):
            heappush(hq, (i[1], i[0]))
print(ans)
