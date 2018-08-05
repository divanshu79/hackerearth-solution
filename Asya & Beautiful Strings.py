a,b = list(map(int,input().split()))
x =[]
for i in range(0,a,1):
	string = input()
	x.append(string)
y = []
count = 0
flag = 0
for i in range(0,b,1):
	st = input()
	for j in range(0,len(x),1):
		q = st+x[j]
		d = {}
		for p in range(65,91,1):
			d[chr(p)]=0
		for k in range(len(q)):
			d[q[k]] += 1
		for s in range(65,91,1):
			if d[chr(s)] == 0:
				flag = 0
				break
			else:
				flag = 1
		if(flag == 1):
			count += 1
print(count)
