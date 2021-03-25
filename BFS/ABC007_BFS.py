from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

c = [list(input()) for r in range(R)]
d =[[float("inf")]*C for i in range(R)]

q = deque([])

def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        y, x = q.popleft()
        if (y == gy and x == gx):
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (d[ny][nx] != float("inf") or
            ny < 0 or nx < 0 or R <= ny or C <= nx or
            c[ny][nx] == "#"):continue
            q.append([ny, nx])
            d[ny][nx] = d[y][x] + 1
    return d[gy][gx]


q.append([sy, sx])
d[sy][sx]=0

print(bfs())

