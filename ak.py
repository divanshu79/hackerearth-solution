for i in range(int(input())):
	a,b = list(map(int,input().split()))
	for i in range(1,a+1,1):
		st = ''
		for j in range(1,b+1,1):
			if(i%2!=0 and j%2!=0):
				st = st+"*"
			elif(i%2==0 and j%2==0):
				st = st+"*"
			else:
				st += "."
		print(st)
