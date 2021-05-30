def DFS1(s,ans):
    if(s <= N and len(C1[s])!=0):
        ans+=1
        if(s in C1[C1[s][0]]):C1[C1[s][0]].remove(s)
        return DFS1(C1[s][0], ans)
    else:
        return int(s), ans


def DFS2(s, ans):
    if(s <= N and len(C2[s]) != 0):
        ans += 1
        if(s in C2[C2[s][0]]):
            C2[C2[s][0]].remove(s)
        return DFS2(C2[s][0], ans)
    else:
        return int(s), ans
    
N = int(input())
A = []
B = []
C1 = [[] for i in range(N+1)]
C2 = [[] for i in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    C1[a].append(b)
    C1[b].append(a)
    C2[b].append(a)
    C2[a].append(b)
    A.append(a)

#端点1の探索
s, ans = DFS1(A[0],0)

#端点2と，そこまでの距離の探索
t, ans = DFS2(s,0)
print(ans+1)
