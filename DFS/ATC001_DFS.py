import sys
sys.setrecursionlimit(500000)

H, W = map(int, input().split())
c = [list(input()) for h in range(H)]

def dfs(h, w):
    if (H <= h or W <= w or w < 0 or h < 0 or c[h][w] == "#"):
        return
    if (c[h][w] == "g"):
        print("Yes")
        exit()
    c[h][w] = "#"
    dfs(h + 1, w)
    dfs(h - 1, w)
    dfs(h, w+1)
    dfs(h, w - 1)
    return

for h in range(H):
    for w in range(W):
        if c[h][w] == "s":
            dfs(h, w)
            break
print("No")
