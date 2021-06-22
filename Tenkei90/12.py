from collections import deque
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def BFS(c, ra, ca, rb, cb):
    Flag = [[False]*H for i in range(W)]
    q = deque([])
    q.append([ra, ca])
    while q:
        x, y = q.popleft()
        for m in move:
            x = x+m[0]
            y = y+m[1]
            if(x >= 0 and y >= 0 and x <= W-1 and y <= H-1 and c[x][y] == True and Flag[x][y]==False):
                q.append([x, y])
                Flag[x][y]=True
                if(x == rb and y == cb):
                    return True
    return False


H, W = map(int, input().split())
m = [[False]*H for i in range(W)]
Q = int(input())
for i in range(Q):
    q = list(map(int, input().split()))
    if(q[0] == 1):
        r, c = q[1], q[2]
        m[r-1][c-1] = True
    else:
        ra, ca, rb, cb = q[1], q[2], q[3], q[4]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if(m[ra][ca] == True and m[rb][cb] == True):
            if(BFS(m, ra, ca, rb, cb)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
