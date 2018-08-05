from collections import defaultdict

n,m = map(int,input().split())
gr = []
cost = []
visit = defaultdict(int)
for _ in range(m):
	x = list(map(int,input().split()))[::-1]
	gr.append(x)

gr.sort()
c = defaultdict(list)
for i in range(len(gr)):
	if(visit[gr[i][1]] == 0 or visit[gr[i][2]] == 0):
		visit[gr[i][1]] = 1
		c[gr[i][1]].append(gr[i][2])
		c[gr[i][2]].append(gr[i][1])
		visit[gr[i][2]] = 1
		cost.append(gr[i][0])

