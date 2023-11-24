'''
Best algorithm for union solution
'''

class QF:
    def __init__(self, N:int) -> None:
        self.N = N
        self.id = [i for i in range(N)]
        self.sz = [1 for i in range(N)]

    def root(self, p:int) -> int:
        while p != self.id[p]:
            self.id[p] = self.id[id[p]]
            p = self.id[p]
        return p

    def is_connected(self, p:int, q:int) -> bool:
        return self.root(p) == self.root(q)

    def union(self, p:int, q:int):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        if self.sz(i) < self.sz(j):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[i] = j
            self.sz[j] += self.sz[i]