c = []
x,y = map(int,input().split())
for i in range(5):
	a = input()
	if('d' in a):
		k = a.index('d')
		c.append(i)
		c.append(k)
		
if(x != c[0] or y != c[1] or (x != c[0] and y != c[1])):
	if(x == c[0]):
		if(y >c[1]):
			print('LEFT')
			y -= 1
		else:
			print('RIGHT')
			y += 1
	else:
		if(x > c[0]):
			print('UP')
			x -= 1
		else:
			print('DOWN')
			x += 1
else:
	print('CLEAN')
