import math
m = 1000000
for i in range(int(input())):
	a = input()
	av = list(set(a))
	#print(a)
	c,v = 0,0
	c1,v1 = 0,0
	flag = 1
	f = math.factorial
	for i in range(len(a)):
		if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u'):
			v += 1
		else:
			c += 1

	for i in range(len(av)):
		if(av[i]=='a' or av[i]=='e' or av[i]=='i' or av[i]=='o' or av[i]=='u'):
			v1 += 1
		else:
			c1 += 1
	if(c != 0):
		if(v == v1 and c == c1):
			x = f(v)%m
			y = f(c)%m
		elif(v == v1 and c != c1):
			x = f(v)%m
			p = f(c)
			q = f(c1)*f(c-c1)
			y = (p//q)%m
		elif(v != v1 and c == c1):
			p = f(v)
			q = f(v1)*f(v-v1)
			x = (p//q)%m
			y = f(c)
		elif(v != v1 and c != c1):
			g = f(v)
			h = f(v1)*f(v-v1)
			x = (g//h)%m
			p = f(c)
			q = f(c1)*f(c-c1)
			y = (p//q)%m
		elif(c==0 or v==0):
			flag = 0
		k = f(c+1)
		l = f(v)*f(c-v+1)
		ans = (((k//l*x)%m)*y)%m
		print(ans)
	else:
		print(-1)
