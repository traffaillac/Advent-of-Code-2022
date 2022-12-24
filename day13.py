from ast import literal_eval
from functools import cmp_to_key
from sys import stdin

def comp(a, b):
	if isinstance(a, int) and isinstance(b, int):
		return a - b
	else:
		if isinstance(a, int):
			a = [a]
		if isinstance(b, int):
			b = [b]
		for i, j in zip(a, b):
			diff = comp(i, j)
			if diff != 0:
				return diff
		return len(a) - len(b)

# part 1
inp = stdin.read()
res = 0
for i, pair in enumerate(inp.split("\n\n")):
	a, b = map(literal_eval, pair.split())
	if comp(a, b) <= 0:
		res += i + 1
print(res)

# part 2
d0, d1 = [[2]], [[6]]
packets = list(map(literal_eval, inp.split())) + [d0, d1]
packets.sort(key=cmp_to_key(comp))
print((packets.index(d0) + 1) * (packets.index(d1) + 1))
