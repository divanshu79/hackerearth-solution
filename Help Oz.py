a = []
for i in range(int(input())):
	n = int(input())
	a.append(n)

x = min(a)
print(max(a))
st = ''
for i in range(2,x,1):
	b = []
	flag = 0
	for j in a:
		if(len(b)==0):
			p = j%i
			b.append(p)
		elif(len(b)!=0):
			q = j%i
			if(q!=b[len(b)-1]):
				flag = 1
				break
			else:
				flag = 0
	if(flag == 0):
		st = st + str(i) + " "

print(st)
			
