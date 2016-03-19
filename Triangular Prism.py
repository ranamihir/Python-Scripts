def minArea(v):
	a = pow(4*v,1.0/3);
	s = 3*a*a*pow(3,1/2.0)/2;
	return s;
t = int(raw_input())
while t:
	vol = int(raw_input())
	print minArea(vol)
	t -= 1
