from sys import stdin

outcomes = {
	"A X": 3, "A Y": 6, "A Z": 0,
	"B X": 0, "B Y": 3, "B Z": 6,
	"C X": 6, "C Y": 0, "C Z": 3}

choices = {
	"A X": 3, "A Y": 1, "A Z": 2,
	"B X": 1, "B Y": 2, "B Z": 3,
	"C X": 2, "C Y": 3, "C Z": 1}

# print(sum(" XYZ".index(line[2]) + outcomes[line] for line in stdin.read().splitlines()))
print(sum("XYZ".index(line[2]) * 3 + choices[line] for line in stdin.read().splitlines()))
	