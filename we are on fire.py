n,m,q = map(int,input().split())
c = []
a = 0
for i in range(n):
	x = list(map(int,input().split()))
	c.append(x)
	a = a+sum(x)

z = 0
for i in range(q):
	u,v = list(map(int,input().split()))
	if(c[u-1][v-1] == 0):
		print(a-z)
	else:
		open = [(u-1,v-1)]
		z += 1
		while(len(open) != 0):
			p = open.pop(0)
			p1 = p[0]
			p2 = p[1]
			c[p1][p2] = 0
			if(p2-1 >= 0 and c[p1][p2-1] == 1):
				z += 1
				c[p1][p2-1] = 0
				open.append((p1,p2-1))
			if(p2+1 <= m-1 and c[p1][p2+1] == 1):
				z += 1
				c[p1][p2+1] = 0
				open.append((p1,p2+1))

			if(p1-1 >= 0 and c[p1-1][p2] == 1):
				z += 1
				c[p1-1][p2] = 0
				open.append((p1-1,p2))
			if(p1+1 <= n-1 and c[p1+1][p2] == 1):
				z += 1
				c[p1+1][p2] = 0
				open.append((p1+1,p2))
		print(a-z)
