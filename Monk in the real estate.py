for _ in range(int(input())):
	a = int(input())
	q = []
	for i in range(a):
		x,y = list(map(int,input().split()))
		if(x not in q):
			q.append(x)
		if(y not in q):
			q.append(y)
	p = len(q)
	print(p)
