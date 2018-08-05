import bisect

u = []
v = []
for _ in range(int(input())):
	a,b,c = list(map(int,input().split()))
	if(a==1):
		u.append(b)
		v.append(c)
	else:
		x = bisect.bisect_left(v,(c-b))
		y = bisect.bisect_left(v,c)
		if(len(v)==y):
			y = y-1

		#print(x)
		#print(y)
		s = 0


		for i in range(x,y+1,1):
			s = s+u[i]
		print(s)
