n, m = map(int, input().split())
a = []
CS = [0]
for i in range(1,n):
    t = int(input())
    CS.append(CS[i-1]+t)
pos = 0
ans = 0
for a in range(m):
    i = (int(input()))
    ans += abs(CS[i+pos]-CS[pos])
    pos += i
print(ans)
