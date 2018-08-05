n = int(input())
a = list(map(int,input().split()))
a = a[::-1]
q,x = list(map(int,input().split()))
b = []
for i in range(q):
	st = input()
	b.append(st)
c = []
flag = 0
for i in range(len(b)):
	if(b[i] == 'Harry'):
		c.append(a[len(a)-1])
		a.pop()
		ans = sum(c)
		if(ans == x):
			print(len(c))
			break
		else:
			if(len(a)==0 and sum(c)!=x):
				flag = 1
	elif(b[i]=='Remove'):
		c.pop()
if(flag == 1):
	print('-1')
