n = int(input())
a = []
for i in range(0,16,1):
	c = 3**i
	if(c<=10000000):
		a.append(c)
	else:
		break
count =0
print(a)
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
	print(str(d)+" "+str(d-n))
