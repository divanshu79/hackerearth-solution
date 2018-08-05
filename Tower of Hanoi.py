for _ in range(int(input())):
	n = int(input())
	a = []
	for i in range(n):
		x,y = list(map(int,input().split()))
		a.append([y,x])
	a.sort(reverse = True)
	print(a)
	arr = []
	for i in range(n-1):
		e = [a[i][0]]
		f = [a[i][1]]
		c = 0
		for j in range(i+1,n):
			if(f[0] > a[j][1]):
				u = e.pop(0)
				v = f.pop(0)
				e.append(a[j][0])
				f.append(a[j][1])
				c += u+e[0]

		arr.append(c)
	print(max(arr))
	print(arr)
