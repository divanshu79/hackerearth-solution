d = {}
d[1] = 1
m = 1000000+4
for i in range(2,m,1):
	d[i] = (d[i-1]*i)%1000003
#print(d)
for i in range(int(input())):
	n,x = list(map(int,input().split()))
	print((d[n]*x)%1000003)
