m = 1000000007
for i in range(int(input())):
	n = int(input())
	if(n == 1):
		print('1')
	else:
		ans = ((n%m)*((2*n-1)%m))%m
		print(ans)
