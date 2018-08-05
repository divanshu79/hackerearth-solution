n = int(input())
a = list(map(int,input().split()))
count = 0
for j in range(int(input())):
	arr = list(map(int,input().split()))
	d = {}
	flag = 0

	for i in range(len(arr)):
		d[arr[i]] = 1

	for i in range(len(a)):
		if(a[i] not in d):
			flag = 1
			break
		else:
			flag = 0
	if(flag == 0):
		count += 1
	#print(d)

print(count)
