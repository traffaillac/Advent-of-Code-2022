from collections import defaultdict
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
H, P = [(0, "AA", "AA", 26, 26, ())], 0
while H:
	p, vy, ve, my, me, o = heappop(H)
	m = max(my, me) - 1
	# if upper bound is greater than best pressure found so far
	if P <= -p + sum((m - i) * f for i, f in enumerate(sorted((f for v, f in F.items() if v not in o), reverse=True)) if m > i):
		if my >= me: # You move first if more remaining time
			for v, f in F.items():
				m = my - D[vy, v] - 1
				if v not in o and m > 0:
					P = max(P, -p + m * f)
					heappush(H, (p - m * f, v, ve, m, me, o + (v,)))
		else: # otherwise elephant moves first
			for v, f in F.items():
				m = me - D[ve, v] - 1
				if v not in o and m > 0:
					P = max(P, -p + m * f)
					heappush(H, (p - m * f, vy, v, my, m, o + (v,)))
print(P)
