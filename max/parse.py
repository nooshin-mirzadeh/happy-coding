#!/usr/bin/python3

from collections import defaultdict
from itertools import chain
from sys import stdout,stderr
from operator import itemgetter, attrgetter, methodcaller

class Endpoint:
    def __init__(self):
        self.ld = None
        self.lc = {}

    def load(self, fob):
        (self.ld, k) = map(int, fob.readline().split())

        for _ in range(k):
            (c, lc) = map(int, fob.readline().split())
            self.lc[c] = lc
        return self


class Problem:

    # p = Problem().load(open('sample'))

    def __init__(self):

        self.s = []
        self.e = []
        # self.r = defaultdict(lambda: 0)
        self.r = []
        self.x = 0

    def load(self, fob):

        (v, e, r, c, self.x) = map(int, fob.readline().split())
        self.s = list(map(int, fob.readline().split()))

        assert len(self.s) == v

        for _ in range(e):
            self.e.append(Endpoint().load(fob))

        for _ in range(r):
            (rv, re, rn) = map(int, fob.readline().split())
            self.r.append((rv,re,rn,rn/self.s[rv]))

        return self

    def sort_request(self):
        self.sr = sorted(self.r, key = itemgetter(3), reverse=True )

class Solution:
    def __init__(self, problem):
        self.cache = defaultdict(set)
        self.cacheusage = defaultdict(lambda: 0)
        self.problem = problem

    def validate():
        for (c, vs) in self.cache.items():
            if sum(self.problem.s[vid] for vid in vs) > self.problem.x:
                return False

        return True

    def is_fit(self, c, v):
        s = self.problem.s[v]
        if self.cacheusage[c] + s > self.problem.x:
            return False
        else:
            return True
    
    def best_place(self, k):
        
        

    def place(self, c, v):
        if v in self.cache[c]:
            return True
        
        s = self.problem.s[v]
        if self.cacheusage[c] + s > self.problem.x:
            return False

        self.cache[c].add(v)
        self.cacheusage[c] += s
        return True


    def saved(self, rv, re):
        e = self.problem.e[re]
        ld = e.ld
        l = ld

        for (c,lc) in e.lc.items():
            if lc < ld and rv in self.cache[c]:
                l = lc

        return ld - l

    def score(self):
        saved = 0
        total = 0
        for (rv,re,rn,_) in self.problem.r:
            saved += rn * self.saved(rv,re)
            total += rn

        return saved / total
        

    def output(self, fd):
        print(len(self.cache), file=fd)
        for (c, vs) in self.cache.items():
            print(" ".join(map(str, chain((c,),vs))))


def greedy(problem):
    pass


def test():
    p = Problem().load(open('sample'))
    p.sort_request()
    print(p.sr)
    s = Solution(p)
    s.place(0,2)
    s.place(1,3)
    s.place(1,1)
    s.place(2,0)
    s.place(2,1)

    print("Saved {}".format(s.score()), file=stderr)

    s.output(stdout)

if __name__ == '__main__':
    test()

