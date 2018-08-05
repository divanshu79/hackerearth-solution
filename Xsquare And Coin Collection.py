m = 1000000
for i in range(int(input())):
	a,b = list(map(int,input().split()))
	x = list(map(int,input().split()))
	s  = []

	for i in range(a):
		if(len(s) == 0 and x[i] <= b):
			s.append(x[i])
		elif(len(s) != 0 and x[i] <= b):
			if(x[i-1] <= b):
				o = s.pop(len(s)-1)
				l = (o+x[i])
				s.append(l)
			else:
				s.append(x[i])
	print(max(s))
