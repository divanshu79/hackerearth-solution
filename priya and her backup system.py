n = int(input())
a = list(map(int,input().split()))
arr = []
for i in range(0,n-1,1):
	x,y = list(map(int,input().split()))
	arr.append([])
	arr[i].append(x)
	arr[i].append(y)
#print(arr[1][0])
#print(arr)

m = int(input())
for i in range(0,m,1):
	u,v = list(map(int,input().split()))
	if(u == 2):
		print((a[v-1])%1000000007)
	elif(u == 1):
		for i in range(0,n-1,1):
			if(v == arr[i][0]):
				a[arr[i][1]-1] = (a[v-1] + a[arr[i][1]-1])%1000000007
				#print(a)
