for i in range(int(input())):
	a = list(map(int,input().split()))
	x = []
	y = []
	for i in range(a[1]):
		b,c = list(map(int,input().split()))
		x.append(b)
		y.append(c)
	for i in range(a[1]):
		if(x[0]>x[len(x)-1]):
			flag = 1
			#print(sum(x)+x[len(x)-1])
		else:
			flag = 0
			#print(sum(x)+x[0])
if(flag == 1):
	print(sum(x)+x[len(x)-1])
else:
	print(sum(x)+x[0])
