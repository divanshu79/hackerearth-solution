n = int(input())
p = list(map(int,input().split()))
v = list(map(int,input().split()))
p.sort()
v.sort()
flag = 0
for i in range(n):
	if(v[i]!=p[i]):
		flag = 1
		break
	else:
		flag = 0
if(flag == 1):
	print("No")
else:
	print("Yes")
