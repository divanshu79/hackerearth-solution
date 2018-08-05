num = input().split()
n = int(num[0])
q = int(num[1])

a = list(map(int,input().split()))
for i in range(0,q,1):
	aa = input().split()
	l = int(aa[0])
	r = int(aa[1])
	count = 0


	for j in range(l-1,r,1):
		x =a[j]
		while(x>0):
			x = int(a[j]/2)
			count += 1
	print(count)
