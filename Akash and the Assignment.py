x,y = list(map(int,input().split()))
st = input()
for i in range(y):
	a,b,c = list(map(int,input().split()))
	t = st[a-1:b]
	#print(t)
	t = sorted(t)
	#print(t)
	#t = list(set(t))
	if(c>len(t)):
		print("Out of range")
	else:
		print(t[c-1])
