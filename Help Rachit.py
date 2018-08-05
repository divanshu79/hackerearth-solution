from random import choice

k = 10001
d,sieve = {},[True]*(k)
for i in range(k):
	d[i] = 0
for i in range(2,k):
	if sieve[i]:
		d[i] = 1
		for j in range(i*i,k,i):
			sieve[j] = False
#print(d)


for _ in range(int(input())):
	n = int(input())
	if(n%2==0):
		x = n*2
	else:
		x = n*2-1

	count = 0
	st = ''
	a = []
	
	for i in range(n):
		b = list(choice(range(3,10001,2)) for _ in range(n))
		#b = list(map(int,input().split()))
		a.append(b)
		
		if(d[b[i]]==1):
			count += 1
			#st = st+str(b[i])+' '
		if(d[b[n-i-1]]==1):
			count += 1
			#st = st+str(b[n-i-1])+' '

	if(n%2!=0 and d[a[n//2][n//2]]==1):
		count -= 1
	#print(st)
	p = (count/x)*100
	q = len(str(int(p)))
	z = "%.6f" %p
	z = int(float(z)*1000000)
	z = str(z)
	z = z[:q]+"."+z[q:len(z)]
	print(z)
