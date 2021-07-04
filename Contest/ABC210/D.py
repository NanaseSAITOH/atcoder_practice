from heapq import heappush, heappop


def sdjkstra(s, g, k, c, n):
    dist = [float("inf")]*n
    dist[s] = 0
    hq = [(0, s)]
    screen = [False]*n
    while hq:
        t = heappop(hq)[1]
        screen[t] = True
        for i in c[t]:
            to, cost = i
            if(screen[to] == False and dist[to] > dist[t]+cost and (to <= k or to == s or to == g)):
                dist[to] = dist[t]+cost
                heappush(hq, (dist[to], to))
    return dist[g]


N, M = map(int, input().split())
c = [[] for i in range(N)]
for i in range(M):
    s, t, d = map(int, input().split())
    c[s-1].append([t-1, d])
ans = 0
for k in range(0, N):
    for s in range(0, N):
        for g in range(0, N):
            a = sdjkstra(s, g, k, c, N)
            if(a != float("inf")):
                ans += a
print(ans)
