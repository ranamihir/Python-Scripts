def modify(a):
	x = bin(a)
	y = x[:1:-1]
	return int(y, 2)
n = int(raw_input())
while n:
	a = int(raw_input())
	x = a
	if not (a & 1):
		x = modify(a)
	print x
	n -= 1
