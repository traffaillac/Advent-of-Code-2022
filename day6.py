buf = input()
for i in range(14, len(buf)):
	if len(set(buf[i-14:i])) == 14: break
print(i)
