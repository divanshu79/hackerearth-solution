n = int(input())
a = []
for i in range(0,16,1):
	c = 3**i
	if(c<=10000000):
		a.append(c)
	else:
		break
count =0
#print(a)
if(n==10000000):
	print(str(0)+" "+str(0))
else:
	for i in range(0,len(a),1):
		if(a[i]<n):
			count += 1
		else:
			count = count
	#print(count)
	d = a[count]
	#print(d)
	flag = 0
	for i in range(len(a)-1,0,-1):
		for j in range(i-1,-1,-1):
			if(d-n>3):
				if(a[i]+a[j]<=(d-n)):
					kl = a[i]+a[j]
					flag = 1
					#print("i "+str(a[i]))
					#print("j "+str(a[j]))
					break
			else:
				kl = d-n
		if(flag == 1):
			break
	print(str(d)+" "+str(kl))
