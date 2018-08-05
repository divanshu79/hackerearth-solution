for _ in range(int(input())):
	n,k = list(map(int,input().split()))
	if(k>1):
		d = {}
		flag = 0
		a = []
		for i in range(n):
			st = input()
			x = len(st)
			a.append(x)
			if(x not in d):
				d[x] = 1
			else:
				d[x] += 1
		a.sort()
		for i in range(len(d)):
			if(d[a[i]]%k!=0):
				flag = 1
				break
		if(flag == 1):
			print("Not possible")
		else:
			print("Possible")
	elif(k == 1):
		for i in range(n):
			st = input()
		print("Possible")
