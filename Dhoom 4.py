a,b = list(map(int,input().split()))
n = int(input())
x = list(map(int,input().split()))
cpyx = x
z = min(x)
lst = [a]
c = 0
flag = 0
m = 100000
while(len(lst)!=0):
	for j in range(len(x)):
		p = (lst[0]*x[j])%m
		if(p>b and (p*z)%m>b):
			cpyx.pop(j)
		else:
			lst.append(p)
		#print(lst)
		if(p==b):
			flag = 1
			break
		if(len(cpyx)==0):
			flag = 0
			break
	lst.pop(0)
	c += 1
	if(flag == 1):
		print(c)
		break
if(len(lst)==0 or flag == 0):
	print('-1')

