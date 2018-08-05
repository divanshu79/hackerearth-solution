a,b = list(map(int,input().split()))
st = input()
st = st[::-1]
x = 1
d = 0
for i in range(0,len(st),1):
	x = x*a
	if(st[i]=="1"):
		d = (d+x)%100
print(d%100)
