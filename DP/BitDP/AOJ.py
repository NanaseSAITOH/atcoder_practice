V, E = map(int, input().split())
path = [[float("inf")]*V for i in range(V)]
for e in range(E):
    s, g, d = map(int, input().split())
    path[s][g] = d
S = 0
dp = [[float("inf")]*(1<<V) for i in range(V)]

dp[0][(1 << V)-1] = 0

print(S)
print(bin(S))

for i in range(S-2,0,-1):
    for v in range(V):
        if(path[v][0]!="inf"):
            dp[v][s] = 
            pass
