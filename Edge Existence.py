d = {}

def graph_int(x):
	for i in range(1,x+1,1):
		d[i] = []

a = int(input())
b = int(input())
graph_int(a)
for _ in range(b):
	x,y = list(map(int,input().split()))
	d[x].append(y)
	d[y].append(x)
#print(d)

q = int(input())
for i in range(q):
	u,v = list(map(int,input().split()))
	if(v in d[u]):
		print('YES')
	else:
		print('NO')
