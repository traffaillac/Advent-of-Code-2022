from string import ascii_lowercase, ascii_uppercase
from sys import stdin

letters = " " + ascii_lowercase + ascii_uppercase

# print(sum(letters.index((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()) for line in stdin))
lines = stdin.read().splitlines()
print(sum(letters.index((set(lines[i]) & set(lines[i+1]) & set(lines[i+2])).pop())
	for i in range(0, len(lines), 3)))
