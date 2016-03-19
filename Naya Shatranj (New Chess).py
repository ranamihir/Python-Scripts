t = int(raw_input())
while t:
	n = int(raw_input())
	if n & 1:
		print "0"
	else:
		print "1"
	t -= 1