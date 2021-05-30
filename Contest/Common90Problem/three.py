def DFS(s,ans):
    if(s <= N and len(G[s])!=0):
        for i in G[s]:
            if(dist[i]==float("inf")):
                dist[i]=ans+1
                DFS(i, dist[i])
    
N = int(input())
A = []
B = []
G = [[] for i in range(N+1)]
C2 = [[] for i in range(N+1)]
dist = [float("inf")]*(N+1)

for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
    A.append(a)

#端点1の探索
dist[A[0]]=0
DFS(A[0],0)
most_big_dist = -1
for i,v in enumerate(dist):
    if(v!=float("inf") and most_big_dist < v):
        most_big_dist = v
        s = i

dist = [float("inf")]*(N+1)
#端点2と，そこまでの距離の探索
DFS(s,0)
most_big_dist = -1
for i, v in enumerate(dist):
    if(v != float("inf") and most_big_dist < v):
        most_big_dist = v
        s = i
print(most_big_dist+1)
