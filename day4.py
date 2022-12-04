from sys import stdin

count = 0
for line in stdin.read().splitlines():
	e, f = line.split(',')
	el, er = map(int, e.split('-'))
	fl, fr = map(int, f.split('-'))
	# count += el<=fl and er>=fr or fl<=el and fr>=er
	count += el<=fr and er>=fl
print(count)
