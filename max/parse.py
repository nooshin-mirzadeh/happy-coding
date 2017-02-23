#!/usr/bin/python3

from collections import defaultdict
from itertools import chain
from sys import stdout,stderr

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
        self.r = defaultdict(lambda: 0)
        self.x = 0

    def load(self, fob):

        (v, e, r, c, self.x) = map(int, fob.readline().split())
        self.s = list(map(int, fob.readline().split()))

        assert len(self.s) == v

        for _ in range(e):
            self.e.append(Endpoint().load(fob))

        for _ in range(r):
            (rv, re, rn) = map(int, fob.readline().split())
            self.r[(rv,re)] = rn 

        return self

class Solution:
    def __init__(self, problem):
        self.cache = {}
        self.problem = problem

    def validate():
        for (c, vs) in self.cache.items():
            if sum(self.problem.s[vid] for vid in vs) > self.problem.x:
                return False

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
        for ((rv,re),rn) in self.problem.r.items():
            saved += rn * self.saved(rv,re)
            total += rn

        return saved / total
        

    def output(self, fd):
        print(len(self.cache), file=fd)
        for (c, vs) in self.cache.items():
            print(" ".join(map(str, chain((c,),vs))))


p = Problem().load(open('sample'))

s = Solution(p)
s.cache[0] = {2}
s.cache[1] = {3,1}
s.cache[2] = {0,1}

print("Saved {}".format(s.score()), file=stderr)

s.output(stdout)

