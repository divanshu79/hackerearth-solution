from collections import defaultdict
a = defaultdict(int)
k = 100000

def pro():
	a[1] = 0
	a[2] = a[3] = 1
	for i in range(4,k,1):
		x = a[i//3] + i%3 + 1
		y = a[i//2] + i%2 + 1
		if(x > y):
			a[i] = y
		else:
			a[i] = x
def abc(n):
	if(n == 1):
		return 0
	if(n <k):
		return(a[n])
	
	x = abc(n//3)+n%3+1
	y = abc(n//2)+n%2+1
	return min(x,y)

pro()
for i in range(int(input())):
	n = int(input())
	if(n>1):
		p = abc(n//3)+n%3+1
		q = abc(n//2)+n%2+1
		print(min(p,q))
	else:
		print(0)
