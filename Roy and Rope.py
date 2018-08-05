for _ in range(int(input())):
	n = int(input())
	ur = list(map(int,input().split()))
	lr = list(map(int,input().split()))
	c = 0
	for i in range(n-1):
		c = max(c,max(ur[i],lr[i])-(n-i-1))
	if(c == 0):
		print(n)
	else:
		print(n+c)
