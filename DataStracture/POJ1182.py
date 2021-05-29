# Union-Find木のソースコード
class UnionFindTree():
    # n要素で初期化
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n

    # 木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # xとyの属する集合を併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # xとyが同じ集合に属するか否か
    def same(self, x, y):
        return self.find(x) == self.find(y)


N, K = map(int, input().split())
txy = [map(int, input().split()) for _ in range(K)]
t, x, y = [list(i) for i in zip(*txy)]

union_find_tree = UnionFindTree(3*N)
ans = 0
for i in range(K):
    if (t[i] == 1):
        if (union_find_tree.same(x[i], y[i] + N) or union_find_tree.same(x[i], y[i] + 2 * N)):
            ans += 1
        else:
            union_find_tree.unite(x[i], y[i])
            union_find_tree.unite(x[i] + N, y[i] + N)
            union_find_tree.unite(x[i] + 2 * N, y[i] + 2 * N)
    if (t[i] == 2):
        if (union_find_tree.same(x[i], y[i]) or union_find_tree.same(x[i] + N, y[i])):
            ans += 1
        else:
            union_find_tree.unite(x[i], y[i] + N)
            union_find_tree.unite(x[i] + N, y[i] + 2 * N)
            union_find_tree.unite(x[i] + 2*N, y[i] + N)
print(ans)
