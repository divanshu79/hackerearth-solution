import bisect

t = int(input())
a = list(map(int,input().split()))
d = []
s = 0
for i in range(len(a)):
	s = s + a[i]
	d.append(s)
q = int(input())
for i in range(q):
	n = int(input())
	if(n>d[len(d)-1]):
		print("-1")
	else:
		x = bisect.bisect_left(d,n)
		print(x+1)
