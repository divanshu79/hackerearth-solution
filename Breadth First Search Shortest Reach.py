from collections import defaultdict

for _ in range(int(input())):
	n,m = map(int,input().split())
	g = defaultdict(list)
	for i in range(m):
		a,b = list(map(int,input().split()))
		g[a].append(b)
		g[b].append(a)

	k = int(input())
	o = [k]
	f = defaultdict(int)
	h = defaultdict(int)
	#h[k] = 1

	while(len(o) != 0):
		p = o.pop(0)
		w = g[p]
		h[p] = 1
		for j in range(len(w)):
			if(h[w[j]] != 1):
				f[w[j]] = f[p] + 6
				o.append(w[j])
				h[w[j]] = 1
		#o.extend(w)
	z = ''
	for i in range(1,n+1):
		if(i != k):
			if(f[i] != 0):
				z = z + str(f[i]) + ' '
			else:
				z = z + '-1' + ' '
	print(z)
