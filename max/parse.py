from collections import defaultdict

class Endpoint:
    def __init__(self):
        self.ld = None
        self.lc = []

    def load(self, fob):
        (self.ld, k) = map(int, fob.readline().split())
        self.lc = [None]*k
        for _ in range(k):
            (c, lc) = map(int, fob.readline().split())
            self.lc[c] = lc
        return self


class Problem:

    # p = Problem().load(open('sample'))

    def __init__(self):

        self.s = []
        self.e = []
        self.r = defaultdict(lambda: 0)

    def load(self, fob):

        (v, e, r, c, x) = map(int, fob.readline().split())
        self.s = list(map(int, fob.readline().split()))

        assert len(self.s) == v

        for _ in range(e):
            self.e.append(Endpoint().load(fob))

        for _ in range(r):
            (rv, re, rn) = map(int, fob.readline().split())
            self.r[(rv,re)] = rn 

        return self


p = Problem().load(open('sample'))
