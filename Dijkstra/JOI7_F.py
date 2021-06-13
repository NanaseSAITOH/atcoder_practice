from heapq import heappush, heappop

def dijkstra(s, c, n):
    screen = [False]*n
    ans = [float("inf")]*n
    hq = [(0,s)]
    while hq:
        now_cost,s=heappop(hq)
        for to, cost in c[s]:
            if(screen[to] == False and ans[to]>now_cost+cost):
                ans[to] = now_cost+cost
                heappush(hq,(ans[to],to))
    return ans

n, k = map(int, input().split())
c = [[] for _ in range(n)]
a = []
for i in range(k):
    ipt = list(map(int, input().split()))
    if(ipt[0] == 1):
        c[ipt[1]-1].append([ipt[2]-1, ipt[3]])
        c[ipt[2]-1].append([ipt[1]-1, ipt[3]])
    else:
        s = ipt[1]-1
        g = ipt[2]-1
        ans = dijkstra(s, c, n)
        if(ans[g]==float("inf")):
            a.append(-1)
        else:
            a.append(ans[g])

for ans in a:
    print(ans)