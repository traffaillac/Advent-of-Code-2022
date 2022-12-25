from sys import stdin

lines = stdin.read().splitlines()

# part 1
intervals = []
for line in lines:
	s, b = line[12:].split(": closest beacon is at x=")
	sx, sy = map(int, s.split(", y="))
	bx, by = map(int, b.split(", y="))
	dist = abs(sx - bx) + abs(sy - by)
	x0 = sx - dist + abs(sy - 2000000) + (by == 2000000 and bx <= sx)
	x1 = sx + dist - abs(sy - 2000000) - (by == 2000000 and bx >= sx)
	if x0 <= x1:
		intervals.append((x0, x1))
intervals.sort()
i, res = 0, 0
while i < len(intervals):
	start, end = intervals[i]
	while i < len(intervals) and intervals[i][0] <= end + 1:
		end = max(end, intervals[i][1])
		i += 1
	res += end - start + 1
print(res)

# part 2
def find(row):
	intervals = []
	for line in lines:
		s, b = line[12:].split(": closest beacon is at x=")
		sx, sy = map(int, s.split(", y="))
		bx, by = map(int, b.split(", y="))
		dist = abs(sx - bx) + abs(sy - by)
		x0 = sx - dist + abs(sy - row)
		x1 = sx + dist - abs(sy - row)
		if x0 <= x1:
			intervals.append((x0, x1))
	intervals.sort()
	i = 0
	start, end = intervals[0]
	while i < len(intervals) and intervals[i][0] <= end + 1:
		end = max(end, intervals[i][1])
		i += 1
	if i < len(intervals):
		print(row + (intervals[i][0] - 1) * 4000000)
for row in range(4000001):
	if row % 100000 == 0:
		print(row)
	find(row)
