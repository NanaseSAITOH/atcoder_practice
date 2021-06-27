import sys
A, B, C, D = map(int, input().split())
flag = True
ans = 0
a = A
c = 0
if(B>C):
    print(-1)
    sys.exit()
while flag:
    a+=B
    c+=C
    if((a/c)<=D):
        flag = False
    ans += 1

print(ans)