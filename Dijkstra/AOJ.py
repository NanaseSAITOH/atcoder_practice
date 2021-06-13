from heapq import heappush, heappop

def sdjkstra(s, v, c):
    dist = [float("inf")]*v
    dist[s]=0
    hq = [(0,s)]
    screen = [False]*v 
    while hq:
        t = heappop(hq)[1]
        screen[t]=True
        for i in c[t]:
            to, cost = i
            if(screen[to]==False and dist[to]>dist[t]+cost):
                dist[to] = dist[t]+cost
                heappush(hq, (dist[to], to))
    return dist


V, E, r = map(int, input().split())
c = [[] for i in range(V)]
for i in range(E):
    s, t, d = map(int, input().split())
    c[s].append([t,d])
ans = sdjkstra(r, V, c)
for a in ans:
    if(a==float("inf")):
        print("INF")
    else:
        print(a)
