from collections import defaultdict
from functools import cache
from heapq import heappush, heappop
from itertools import product
from pprint import pprint
from re import findall
from sys import stdin

# adapted from a nice Reddit post
R = r'Valve (\w+) .*=(\d+); .* valves? (.*)'
V, F, D = [], {}, defaultdict(lambda: 100)
for v, f, W in findall(R, stdin.read()):
	V.append(v)
	if f != '0':
		F[v] = int(f)
	for w in W.split(", "):
		D[v, w] = 1
for k, i, j in product(V, V, V):    # floyd-warshall
	D[i,j] = min(D[i,j], D[i,k] + D[k,j])
# 20*24+21*23+35*19+2*17+3*15
@cache
def part1(v, c, m):
	return max((F[w] * (m - D[v, w] - 1) + part1(w, c - {w}, m - D[v, w] - 1)
		for w in c if m - D[v, w] > 1), default=0)
print(part1("AA", frozenset(F), 30))
@cache
def part2(v, c, m):
	return max([F[w] * (m - D[v, w] - 1) + part2(w, c - {w}, m - D[v, w] - 1)
		for w in c if m - D[v, w] > 1] + [part1("AA", c, 26)])
print(part2("AA", frozenset(F), 26))
