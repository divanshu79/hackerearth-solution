n,m = list(map(int,input().split()))
d = {}
for i in range(n):
	a = list(map(int,input().split()))
	l = 0
	for x in a:
		d[x] = (i,l)
		l += 1


q = int(input())
for i in range(q):
	s = int(input())

	if(s in d):
		print(str(d[s][0])+" "+str(d[s][1]))
	else:
		print("-1 "+"-1")
