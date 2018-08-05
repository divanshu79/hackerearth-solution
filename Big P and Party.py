from collections import defaultdict

n,m = map(int,input().split())
g = defaultdict(list)
for _ in range(m):
	a,b = map(int,input().split())
	g[a].append(b)
	g[b].append(a)
open = [0]
close = defaultdict(int)
close[0] = 1
value = defaultdict(int)
while(len(open) != 0):
	p = open.pop(0)
	#close[p] = 1
	k = g[p]
	for i in range(len(k)):
		if(close[k[i]] == 0):
			open.append(k[i])
			value[k[i]] = value[p] + 1
			close[k[i]] = 1
print(value)
for i in range(1,n):
	if(value[i] != 0):
		print(value[i])
	else:
		print('INF')
