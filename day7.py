from collections import defaultdict
from sys import stdin

# by convention, key 0 is the parent and 1 is the size
lambdadict = lambda: defaultdict(lambdadict)
root = defaultdict(lambdadict)
cur = root
for line in stdin.read().splitlines():
	if line[0] == '$':
		arg = line[5:]
		if arg == '/':
			cur = root
		elif arg == "..":
			cur = cur[0]
		elif arg != '':
			cur[arg][0] = cur
			cur = cur[arg]
	else:
		type, name = line.split()
		if type == "dir":
			cur[name][0] = cur
		else:
			cur[name] = int(type)

sizes = []
def rec(node):
	if isinstance(node, int):
		s = node
	else:
		s = sum(rec(v) for k, v in node.items() if not isinstance(k, int))
		sizes.append(s)
	return s
rec(root)
# print(sum(s for s in sizes if s <= 100_000))
sizes.sort()
need = sizes[-1] - 40_000_000
print(next(s for s in sizes if s >= need))
