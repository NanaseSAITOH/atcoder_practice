class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
H, W = map(int, input().split())
m = [[False]*W for i in range(H)]
Q = int(input())
union_find = UnionFind(H*W)
for i in range(Q):
    q = list(map(int, input().split()))
    if(q[0] == 1):
        r, c = q[1], q[2]
        r -= 1
        c -= 1
        m[r][c] = True
        for ido in move:
            if(r+ido[0]>=0 and c+ido[1]>=0 and r+ido[0]<H and c+ido[1]<W):
                if(m[r+ido[0]][c+ido[1]]==True):
                    union_find.union(r*W+c,(r+ido[0])*W+c+ido[1])
    else:
        ra, ca, rb, cb = q[1], q[2], q[3], q[4]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if(m[ra][ca] == True and m[rb][cb] == True):
            if(union_find.same(ra*W+ca,rb*W+cb)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
