from sys import stdin

# print(max(sum(int(line) for line in elf.split()) for elf in stdin.read().split("\n\n")))
print(sum(list(sorted(sum(int(line) for line in elf.split()) for elf in stdin.read().split("\n\n")))[-3:]))
