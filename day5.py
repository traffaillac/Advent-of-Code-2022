from collections import defaultdict
from sys import stdin

stacks = defaultdict(list)
while True:
	line = stdin.readline()
	if line[1] == '1': break
	for i in range(1, len(line), 4):
		if line[i] != ' ':
			stacks[i // 4].insert(0, line[i])
stdin.readline()
for line in stdin:
	_, num, _, src, _, dst = line.split()
	# for _ in range(int(num)):
	# 	stacks[int(dst)-1].append(stacks[int(src)-1].pop())
	stacks[int(dst)-1].extend(stacks[int(src)-1][-int(num):])
	stacks[int(src)-1] = stacks[int(src)-1][:-int(num)]
print(''.join(stacks[i][-1] for i in range(len(stacks))))
