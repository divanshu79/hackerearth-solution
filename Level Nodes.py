d = {}
q = {}
r = {}
lis = [1]
check = [1]
def graph(x):
	for i in range(1,x+1,1):
		d[i] = []
		q[i] = 1
		r[i] = 0
r[1] = 1

n = int(input())
graph(n)
for i in range(n-1):
	a,b = list(map(int,input().split()))
	d[a].append(b)
	d[b].append(a)

for i in range(len(d)):
	while(len(check)!=0):
		s = len(d[check[0]])
		p = d[check[0]]
		for j in range(s):
			if(p[j] not in lis):
				check.append(p[j])
				lis.append(p[j])
				r[q[p[j]] + q[check[0]]] += 1
				q[p[j]] += q[check[0]]
		check.pop(0)
x = int(input())
print(r[x])
