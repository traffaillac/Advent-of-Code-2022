from string import ascii_lowercase
from sys import stdin

# input
grid = list(map(list, stdin.read().splitlines()))
R, C = len(grid), len(grid[0])
rs, cs = next((r, c) for r, l in enumerate(grid) for c, e in enumerate(l) if e == 'S')
re, ce = next((r, c) for r, l in enumerate(grid) for c, e in enumerate(l) if e == 'E')
grid[rs][cs] = 'a'
grid[re][ce] = 'z'

# part 1
queued = [[False] * len(l) for l in grid]
queued[rs][cs] = True
queue = [(rs, cs)]
steps = 0
while not queued[re][ce]:
	new = []
	for r, c in queue:
		e = ascii_lowercase.index(grid[r][c])
		for dr, dc in ((-1,0), (0,-1), (0,1), (1,0)):
			if 0 <= r+dr < R and 0 <= c+dc < C and not queued[r+dr][c+dc] and\
				ascii_lowercase.index(grid[r+dr][c+dc]) <= e + 1:
				queued[r+dr][c+dc] = True
				new.append((r+dr, c+dc))
	queue = new
	steps += 1
print(steps)

# part 2
queued = [[False] * len(l) for l in grid]
queued[re][ce] = True
queue = [(re, ce)]
steps = 0
while all(grid[r][c] != 'a' for r, c in queue):
	new = []
	for r, c in queue:
		e = ascii_lowercase.index(grid[r][c])
		for dr, dc in ((-1,0), (0,-1), (0,1), (1,0)):
			if 0 <= r+dr < R and 0 <= c+dc < C and not queued[r+dr][c+dc] and\
				ascii_lowercase.index(grid[r+dr][c+dc]) >= e - 1:
				queued[r+dr][c+dc] = True
				new.append((r+dr, c+dc))
	queue = new
	steps += 1
print(steps)
