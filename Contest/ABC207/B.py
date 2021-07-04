import sys
A, B, C, D = map(int, input().split())
if(D*C==B):
    print(-1)
    sys.exit()
n = int(A/(D*C-B))
if(D*C-B > 0):
    print(n+1)
else:
    print(-1)
