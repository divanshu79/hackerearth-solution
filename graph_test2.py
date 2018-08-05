d = {}

def graph_int(x):
	for i in range(1,x+1,1):
		d[i] = []

a = int(input())
b = int(input())
graph_int(a)
for _  in range(b):
	x,y = list(map(int,input().split()))
	d[x].append(y)

u = [1,2,3,4]
def big_len(z):
	st = ''
	r = 'Adjacency list of node' +str(z)+':'
	for i in range(len(d[z])):
		st = st + str(d[z][i]) + ' -->'
	st = st[::-1]
	st = st[3:]
	st = st[::-1]
	print(r+st)

	
for i in range(1,a+1,1):
	e = i
	if(len(d[i])<=1):
		st = 'Adjacency list of node'+ str(i)+':' +str(d[i][0])
		print(st)
	else:
		big_len(i)
		#print(st)


