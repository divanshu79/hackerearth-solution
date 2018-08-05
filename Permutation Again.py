d = {}
k = p = 0
d[1] = d[2] = 1
d[3] = 3
d[4] = 7
for i in range(5,100001,1):
	if(i%2!=0):
		d[i] = d[i-2] + 8 + k
		k += 4
		#d[i] = ans
	else:
		d[i] = d[i-2] + 10 + p
		p += 4

for _ in range(int(input())):
	n = int(input())

	print(d[n])
