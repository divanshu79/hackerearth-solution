c = []
n = int(input())
for i in range(n):
	a = input()
	if('p' in a):
		k = a.index('p')
		c.append(i)
		c.append(k)
x = n//2
for i in range(abs(c[0]-x)):
	if(c[0] > x):
		print('DOWN')
	else:
		print("UP")
		
for i in range(abs(c[1]-x)):
	if(c[1] > x):
		print('RIGHT')
	else:
		print('LEFT')
