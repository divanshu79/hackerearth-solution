for i in range(int(input())):
	a,b = input().split()
	a = int(a)
	b = int(b)
	count = 0
	for i in range(a,b+1,1):
		if(i==1):
			count += 1
		else:
			x = i**(1/2)
			flag = 0
			for j in range(2,int(x),1):
				if(i%j==0):
					flag += 1
			if((flag+2)%2!=0):
				count += 1
			print(flag)

	print(count)
