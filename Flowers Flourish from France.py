def answer(a):
	b = a.split()
	s = b[0][0].lower()
	check = True
	for i in b:
		if (i[0].lower() != s):
			check = False
			break
	if check:
		return 'Y'
	else:
		return 'N'
a = raw_input()
while a != "*":
	print answer(a)
	a = raw_input()