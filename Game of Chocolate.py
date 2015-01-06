from fractions import gcd
t = int(raw_input())
for i in range(1, t+1):
	[x1, y1, x2, y2] = map(int, raw_input().split())
	d = (x1 + y1) * (x2 + y2 + 1)
	n = x1 * (x2 + 1) + y1 * (y2 + 1)
	if d == 0 or n == 0:
		print 'Case', str(i)+': 0'
	else:
		g = gcd(n, d)
		print 'Case', str(i)+':', str(n/g)+'/'+str(d/g)