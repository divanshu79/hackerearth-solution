t,n = list(map(int,input().split()))
d = {}
x = n
s = {}
for i in range(1,x//2+1):
	s[i] = 0
s[1] = 1
for i in range(1,x+1):
	d[i] = 1

for i in range(2,x+1):
	count = 0
	for j in range(1,i//2+1):
		if(i%j==0):
			count += 1
	d[i] += count
	s[count+1] += 1
#print(d)
#print(s)




for _ in range(t):
	k = int(input())
	a = d[k]
	summ = 0
	for i in range(1,a,1):
		summ += s[i]

	print(summ)
