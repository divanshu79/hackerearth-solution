from collections import defaultdict

n,m = map(int,input().split())
a = []
for i in range(n):
	b = []
	for j in range(n):
		b.append(0)
	a.append(b)
#print(a)

d = defaultdict(list)

for i in range(m):
	x = list(map(int,input().split()))
	if(x[0] == 2):
		d[x[1]-1].append(x[2]-1)
		#a[x[1]-1][x[2]-1] = 1
		open = [x[2]-1]
		c = defaultdict(int)
		c[x[1]-1] = 1
		w = a[0][x[1]-1]
		if(w == 0 and x[1] != 1):
			a[x[1]-1][x[2]-1] = 1
		elif(x[1] != x[2]):
			if(x[1] != 1):
				a[0][x[2]-1] = a[0][x[1]-1] + 1
			else:
				a[0][x[2]-1] = 1
			while(len(open) != 0):
				p = open.pop(0)
				s = d[p]
				for j in range(len(s)):
					if(c[s[j]] == 0):
						open.append(s[j])
						c[s[j]] = 1
						o = a[0][p] + 1
						if(a[0][s[j]] == 0):
							a[0][s[j]] = o
						else:
							a[0][s[j]] = min(o,a[0][s[j]])

	elif(x[0] == 1):
		t = a[0][x[1]-1]
		if(t == 0 and x[1] != 1):
			print('-1')
		elif(t == 0 and x[1] == 1):
			print('0')
		else:
			print(t)
