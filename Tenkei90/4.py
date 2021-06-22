H, W = map(int, input().split())
ch = [[-1]*W for i in range(H)]
cw = [[-1]*W for i in range(H)]
ans = [[-1]*W for i in range(H)]
c = []
for h in range(H):
    c.append(list(map(int, input().split())))
for h in range(H):
    for w in range(W):
        if(w==0):
            ch[h][w] = c[h][w]
        else:
            ch[h][w] = ch[h][w-1]+c[h][w]

for w in range(W):
    for h in range(H):
        if(h == 0):
            cw[h][w] = c[h][w]
        else:
            cw[h][w] = cw[h-1][w]+c[h][w]

for h in range(H):
    for w in range(W):
        ans[h][w]=ch[h][W-1]+cw[H-1][w]-c[h][w]

for a in ans:
    print(*a)
