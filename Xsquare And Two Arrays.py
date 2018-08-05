n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

u = [0,a[0]]
v = [0,b[0]]
for i in range(2,n+1):
	if(i%2 == 0):
		u.append(b[i-1]+u[len(u)-1])
		v.append(a[i-1]+v[len(v)-1])
	else:
		u.append(a[i-1]+u[len(u)-1])
		v.append(b[i-1]+v[len(v)-1])
#print(u)
#print(v)

for i in range(m):
	x = list(map(int,input().split()))
	if((x[1])%2 == 0 and x[0] == 1):
		print(v[x[2]] - v[x[1]-1])
		
	elif((x[1])%2 == 0 and x[0] == 2):
		p = u[x[2]] - u[x[1]-1]
		print(p)
		
	elif((x[1])%2 != 0 and x[0] == 1):
		p = u[x[2]] - u[x[1]-1]
		print(p)
		
	elif((x[1])%2 != 0 and x[0] == 2):
		print(v[x[2]] - v[x[1]-1])
