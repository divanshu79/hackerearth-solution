list = [0,1,2,2,1]
#print(a)
for i in range(int(input())):
	a = int(input())
	sq = a**(1/2.0)
	z = int(sq)
	count = 0
	flag = 0
	if(sq == z):
		flag = 1
		print("1")
	elif(sq != z):
		while(a>4):
			s = a**(1/2.0)
			b = int(s)
			a = a - (b**2)
			count += 1
			#print(z)
			#print(a)
	#print(a)
		print(count+list[a])
