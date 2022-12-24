from sys import stdin

# stats on input
paths = stdin.read().splitlines()
base, end, rows = 500, 500, 0
for path in paths:
	for point in path.split(" -> "):
		x, y = map(int, point.split(','))
		base = min(base, x - 1)
		end = max(end, x + 2)
		rows = max(rows, y + 1)
cols = end - base
print(base, rows, cols)

# part 1
grid = [['.'] * cols for _ in range(rows)]
for path in paths:
	points = [tuple(map(int, point.split(','))) for point in path.split(" -> ")]
	for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
		while True:
			grid[y0][x0-base] = '#'
			if x0==x1 and y0==y1:
				break
			x0 += min(max(x1 - x0, -1), 1)
			y0 += min(max(y1 - y0, -1), 1)
r, c, units = 0, 500 - base, 0
while True:
	if r+1 == rows:
		break
	elif grid[r+1][c] == '.':
		r += 1
	elif grid[r+1][c-1] == '.':
		r += 1
		c -= 1
	elif grid[r+1][c+1] == '.':
		r += 1
		c += 1
	else:
		grid[r][c] = 'o'
		units += 1
		r, c = 0, 500 - base
print('\n'.join(''.join(l) for l in grid))
print(units)

# part 2
grid = [['.'] * (rows * 2 + 5) for _ in range(rows + 1)]
grid.append(['#'] * (rows * 2 + 5))
for path in paths:
	points = [tuple(map(int, point.split(','))) for point in path.split(" -> ")]
	for (x0, y0), (x1, y1) in zip(points[:-1], points[1:]):
		while True:
			grid[y0][x0-500+rows+2] = '#'
			if x0==x1 and y0==y1:
				break
			x0 += min(max(x1 - x0, -1), 1)
			y0 += min(max(y1 - y0, -1), 1)
r, c, units = 0, rows + 2, 0
while grid[0][rows+2] == '.':
	if grid[r+1][c] == '.':
		r += 1
	elif grid[r+1][c-1] == '.':
		r += 1
		c -= 1
	elif grid[r+1][c+1] == '.':
		r += 1
		c += 1
	else:
		grid[r][c] = 'o'
		units += 1
		r, c = 0, rows + 2
print('\n'.join(''.join(l) for l in grid))
print(units)
