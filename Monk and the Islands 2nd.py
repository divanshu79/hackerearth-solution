from collections import defaultdict

for _ in range(int(input())):
	a,b = list(map(int,input().split()))
	g = defaultdict(list)
	for i in range(b):
		x,y = list(map(int,input().split()))
		g[x].append(y)
		g[y].append(x)
	#print(g)

	open = [(0,1)]
	close = []
	c = d = {}
	for i in range(2,a+1):
		c[i] = 1000000
		d[i] = 0
	d[1] = 1
	c[1] = 1
		
	while(len(open)!=0):
		#open.sort()
		p = open.pop(0)
		if(d[p[1]] < c[p[1]]):
			c[p[1]] = d[p[1]]
		close.append(p[1])
		v = g[p[1]]
		flag = 0
		if(a in v):
			flag = 1
			q = p[0] + 1
		for i in range(len(v)):
			if(v[i] not in close):
				d[v[i]] = p[0] + 1
				open.append((d[v[i]],v[i]))
		if(flag == 1):
			print(q)
			break
		
