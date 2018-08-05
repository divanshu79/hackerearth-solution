for i in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	b = []
	st = ''
	c = []
	for i in range(len(a)):
		if(len(b)==0):
			b.append(a[i])
			st = st+'1' + ' '
			c.append(1)
		else:
			if(b[len(b)-1]>a[i]):
				b.append(a[i])
				st += '1' + ' '
				c.append(1)
			else:
				s = 1
				for j in range(len(c)):
					if(a[i]>=b[len(b)-1]):
						s = s + c[len(c)-1]
						b.pop()
						c.pop()
						if(len(b)==0):
							b.append(a[i])
							st += str(s-1)+' '
							c.append(s)
							break
					elif(a[i]<b[len(b)-1]):
						b.append(a[i])
						st += str(s)+' '
						c.append(s)
						break
	print(st)
