for i in range(int(input())):
	a,b,c = list(map(int,input().split()))
	if(c==0):
		print(int(a/b))
	else:
		x = a/b
		k = len(str(int(x)))
		y = pow(10,c)
		#print("y is " +str(y))
		z = str(int(x*y))
		if(a>=b):
                        z = z[:k]+'.'+z[k:]
                elif(a<b):
                        z = '0.'+z
                print(z)
