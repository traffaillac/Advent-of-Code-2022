from sys import stdin

x, y = [0] * 10, [0] * 10
visited = set()
for line in stdin.read().splitlines():
	dir, steps = line.split()
	for i in range(int(steps)):
		x[0] += {'U':0, 'D':0, 'L':-1, 'R':1}[dir]
		y[0] += {'U':1, 'D':-1, 'L':0, 'R':0}[dir]
		for j in range(9):
			if x[j] == x[j+1] + 2 and y[j] == y[j+1]:
				x[j+1] += 1
			elif x[j] == x[j+1] - 2 and y[j] == y[j+1]:
				x[j+1] -= 1
			elif y[j] == y[j+1] + 2 and x[j] == x[j+1]:
				y[j+1] += 1
			elif y[j] == y[j+1] - 2 and x[j] == x[j+1]:
				y[j+1] -= 1
			elif abs(x[j]-x[j+1]) > 1 or abs(y[j]-y[j+1]) > 1:
				x[j+1] += min(max(x[j]-x[j+1], -1), 1)
				y[j+1] += min(max(y[j]-y[j+1], -1), 1)
		visited.add((x[9], y[9]))
print(len(visited))
