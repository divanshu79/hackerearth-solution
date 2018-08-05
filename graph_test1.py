l_out = []
#l_in = []
def int_graph(x,y):
	for i in range(x):
		l_in = []
		for j in range(y):
			l_in.append('0')
		l_out.append(l_in)

print(l_out)


node = int(input())
edge = int(input())

int_graph(node,edge)
for i in range(edge):
	x,y = list(map(int,input().split()))
	l_out[x-1][y-1] = '1'
print(l_out)
