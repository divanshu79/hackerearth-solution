import bisect
from collections import defaultdict


#print(ps)


k = int(input())
ps = [0]
pss = defaultdict(int)
se = [True]*k

for p in range(2,k):
	if(se[p]):
		ps.append(p)
		pss[p] = 1
		for i in range(p*p,k,p):
			se[i] = False


x = list(map(int,input().split()))
y = x.sort()
s = []
for i in range(len(y)):
	p = x.index(y[i])
	if(pss[p-1] == 1):
		
