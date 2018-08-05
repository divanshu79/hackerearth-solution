l_out = []

def graph(x):
	for i in range(1,x+1):
		l_in = []
		for j in range(1,x+1):
			l_in.append(100000)
		l_out.append(l_in)


for _ in range(int(input())):
	a,b = list(map(int,input().split()))
	p = max(a,b)
	graph(p)
	#print(p)
	print(l_out)
	for i in range(b):
		x,y = list(map(int,input().split()))
		l_out[x-1][y-1] = 1
		l_out[y-1][x-1] = 1

	for k in range(p):
		for i in range(p):
			for j in range(p):
				u = l_out[i][k]+l_out[k][j]
				v = l_out[i][j]
				if(u < v):
					l_out[i][j] = l_out[i][k]+l_out[k][j]

	print(l_out[0][p-1])
	l_out = []
