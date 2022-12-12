from dataclasses import dataclass
from math import lcm
from typing import Callable

@dataclass
class Monkey:
	items: list
	op: Callable
	div: int
	iftrue: int
	iffalse: int
	inspect: int = 0
'''monkeys = [
	Monkey([79, 98], lambda i: i * 19, 23, 2, 3),
	Monkey([54, 65, 75, 74], lambda i: i + 6, 19, 2, 0),
	Monkey([79, 60, 97], lambda i: i * i, 13, 1, 3),
	Monkey([74], lambda i: i + 3, 17, 0, 1)
]'''
monkeys = [
	Monkey([56, 52, 58, 96, 70, 75, 72], lambda i: i * 17, 11, 2, 3),
	Monkey([75, 58, 86, 80, 55, 81], lambda i: i + 7, 3, 6, 5),
	Monkey([73, 68, 73, 90], lambda i: i * i, 5, 1, 7),
	Monkey([72, 89, 55, 51, 59], lambda i: i + 1, 7, 2, 7),
	Monkey([76, 76, 91], lambda i: i * 3, 19, 0, 3),
	Monkey([88], lambda i: i + 4, 2, 6, 4),
	Monkey([64, 63, 56, 50, 77, 55, 55, 86], lambda i: i + 8, 13, 4, 0),
	Monkey([79, 58], lambda i: i + 6, 17, 1, 5)
]
mod = lcm(*(m.div for m in monkeys))
for round in range(10000):
	for m in monkeys:
		m.inspect += len(m.items)
		for item in m.items:
			item = m.op(item) % mod
			monkeys[m.iftrue if item % m.div == 0 else m.iffalse].items.append(item)
		m.items.clear()
inspect = list(sorted(m.inspect for m in monkeys))
print(inspect[-1] * inspect[-2])
