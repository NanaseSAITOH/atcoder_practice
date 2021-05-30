N, K = map(int,input().split())
A=[]
B=[]
C=[]
for n in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append([a,b])

C= sorted(C)
money = K
dist = 0
dist += money
money -= K
for i in range(N):
    if(C[i][0]<=dist):
        money+=C[i][1]
    if(money==0):
        break
    dist += C[i][1]
    money -= C[i][1]
print(dist)
