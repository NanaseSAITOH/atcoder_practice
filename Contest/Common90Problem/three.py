def DFS(s,ans):
    if(s <= N and len(G[s])!=0):
        for i in G[s]:
            if(dist[i] == 10**5):
                dist[i]=ans+1
                DFS(i, dist[i])
    
N = int(input())
A = []
B = []
G = [[] for i in range(N+1)]
C2 = [[] for i in range(N+1)]
dist = [10**5]*(N+1)

for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

#端点1の探索
dist[1]=0
DFS(1,0)
most_big_dist = -1
for i,v in enumerate(dist):
    if(v != 10**5 and most_big_dist < v):
        most_big_dist = v
        s = i

dist = [10**5]*(N+1)
#端点2と，そこまでの距離の探索
DFS(s,0)
most_big_dist = -1
for i, v in enumerate(dist):
    if(v != 10**5 and most_big_dist < v):
        most_big_dist = v
        s = i
print(most_big_dist+1)
