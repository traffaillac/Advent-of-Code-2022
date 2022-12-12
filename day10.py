v = 1
inc = None
crt = ['.'] * 240
for cycle in range(240):
	if v-1 <= cycle % 40 <= v+1:
		crt[cycle] = '#'
	if inc != None:
		v += inc
		inc = None
	else:
		try: op = input()
		except: break
		if op != "noop":
			inc = int(op.split()[1])
print('\n'.join(''.join(crt[i:i+40]) for i in range(0, 240, 40)))
