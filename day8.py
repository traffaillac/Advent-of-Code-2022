from sys import stdin

grid = stdin.read().splitlines()
R, C = len(grid), len(grid[0])

visibles = {(r, c) for r in range(R) for c in range(C) if r==0 or c==0 or r==R-1 or c==C-1}
for r in range(1, R-1):
	h = grid[r][0]
	for c in range(1, C-1):
		if grid[r][c] > h:
			h = grid[r][c]
			visibles.add((r, c))
	h = grid[r][C-1]
	for c in range(C-2, 0, -1):
		if grid[r][c] > h:
			h = grid[r][c]
			visibles.add((r, c))
for c in range(1, C-1):
	h = grid[0][c]
	for r in range(1, R-1):
		if grid[r][c] > h:
			h = grid[r][c]
			visibles.add((r, c))
	h = grid[R-1][c]
	for r in range(R-2, 0, -1):
		if grid[r][c] > h:
			h = grid[r][c]
			visibles.add((r, c))
# print(len(visibles))

score = 0
for r in range(1, R-1):
	for c in range(1, C-1):
		h = grid[r][c]
		up = next(n for n in range(1, R) if grid[r-n][c]>=h or r-n==0)
		left = next(n for n in range(1, C) if grid[r][c-n]>=h or c-n==0)
		right = next(n for n in range(1, C) if grid[r][c+n]>=h or c+n==C-1)
		down = next(n for n in range(1, R) if grid[r+n][c]>=h or r+n==R-1)
		score = max(score, up*left*right*down)
print(score)
