import itertools

a,b = list(map(int,input().split()))
arr = list(map(int,input().split()))
for i in range(len(arr)):
	arr[i] = arr[i]%10
#print(arr)

z = list(itertools.combinations(arr,b))
c = []
for i in range(len(z)):
	x = (z[i][0])%10 + (z[i][1])%10
	c.append(x%10)

print(max(c))
