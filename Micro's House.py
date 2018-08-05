from collections import defaultdict

a,b = list(map(int,input().split()))
g = defaultdict(list)
for i in range(a):
	x = list(map(int,input().split()))
	g[0].append(x)

p = g[0]
l = []
w = []
for i in range(b):
	z = 0
	for j in range(a):
		z = z^p[j][i]
		l.append(z)

for i in range(a):
	q = 0
	for j in range(b):
		q = q^p[i][j]
		w.append(q)
if(max(l) >max(w)):
	print(max(l))
else:
	print(max(w))
