n = int(input())
a = list(map(int,input().split()))
p = 1
s = 1
m = 1000000007
b = []
for i in range(len(a)):
	if(a[i]==0):
		b.append(i)
	else:
		p = ((p%m)*(a[i]%m))%m
#print(b)
for i in range(int(input())):
	y = list(map(int,input().split()))
	if(y[0]==1):
		if(len(b)!=0):
			if(len(b)==1):
				if((y[1]-1) in b):
					ans = p//a[y[1]-1]
					print(int(ans))
				else:
					print('0')
			elif(len(b)>1):
				print('0')
		else:
			ans = p//a[y[1]-1]
			print(int(ans))
	else:
		if(y[2]==0):
			b.append(y[1])
		else:
			if(y[1]>len(a)):
				a.append(y[2])
				p = (p*y[2])%m
			else:
				if((y[1]-1) in b):
					b.remove(y[1]-1)
					p = (p*y[2])%m
				else:
					p = ((p*y[2])/a[y[1]-1])%m
			
	#print(len(b))
