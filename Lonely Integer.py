from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))
f = defaultdict(int)
a = []
for i in range(len(arr)):
	if(f[arr[i]] == 0):
		a.append(arr[i])
		f[arr[i]] += 1
	elif(f[arr[i]] == 1):
		b = a.index(arr[i])
		s = a.pop(b)
		f[arr[i]] += 1
	print(a)
