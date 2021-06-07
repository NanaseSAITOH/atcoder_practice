from collections import deque

N, M = map(int,input().split())
A = []
B = []
c = [[] for r in range(N)]
for i in range(M):
    a, b = map(int,input().split())
    c[a-1].append(b-1)

q = deque([])
flag = [True for i in range(N)]
ans = 0
def bfs(ans):
    while q:
        s = q.popleft()
        g = c[s]
        for i in range(len(g)):
            nx = g[i]
            if (flag[nx]==False):
                continue
            q.append(nx)
            flag[nx]=False
            ans+=1
    return ans


q.append(0)
flag = [True for i in range(N)]

for i in range(N):
    ans += 1
    q.append(i)
    flag = [True for i in range(N)]
    flag[i]=False
    ans = bfs(ans)
print(ans)
