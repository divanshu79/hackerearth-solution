c = []
n = int(input())
x,y = map(int,input().split())
for i in range(n):
	a = input()
	if('p' in a):
		k = a.index('p')
		c.append(i)
		c.append(k)

if(x == c[0]):
	if(y >c[1]):
		print('LEFT')
	else:
		print('RIGHT')
else:
	if(x > c[0]):
		print('UP')
	else:
		print('DOWN')
