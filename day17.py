from sys import stdin

shapes = (
	((0, 0), (0, 1), (0, 2), (0, 3)),
	((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
	((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
	((0, 0), (1, 0), (2, 0), (3, 0)),
	((0, 0), (0, 1), (1, 0), (1, 1)))
grid = ["#######"] + [['.'] * 7 for _ in range(7)]
jets = stdin.read()
j, si, sr, sc = 0, 0, 4, 2
C, H = {}, []
while True:
	if jets[j] == '<':
		if sc > 0 and all(grid[sr+r][sc-1+c]=='.' for r, c in shapes[si % 5]):
			sc -= 1
	else:
		if all(sc+c+1<7 and grid[sr+r][sc+1+c]=='.' for r, c in shapes[si % 5]):
			sc += 1
	j = 0 if j == len(jets) - 1 else j + 1
	if all(grid[sr-1+r][sc+c]=='.' for r, c in shapes[si % 5]):
		sr -= 1
	else:
		key = si%5, j, ''.join(''.join(l) for l in grid[-34:])
		H.append(len(grid) - 8)
		if key in C:
			break
		C[key] = si
		for r, c in shapes[si % 5]:
			grid[sr+r][sc+c] = "#"
		while "#" in grid[-7]:
			grid.append(["."] * 7)
		si, sr, sc = si + 1, len(grid) - 4, 2
# print(len(grid) - 8)
div = (1_000_000_000_000 - C[key]) // (si - C[key])
rem = (1_000_000_000_000 - C[key]) % (si - C[key])
print(div * (H[si] - H[C[key]]) + H[C[key] + rem])
