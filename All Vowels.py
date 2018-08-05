a = ['a','e','i','o','u']
n = int(input())
st = input()
d = {}
flag = 0
for i in range(len(st)):
	d[st[i]] = 1

		
for i in range(len(a)):
	if(a[i] in d):
		flag = 1
	else:
		flag = 0
		break

		
if(flag == 1):
	print("YES")
else:
	print("NO")
