for i in range(int(input())):
	a = list(map(int,input().split()))
	s = a[0]
	k = a[len(a)-1]
	ans = int((k/s)**(1/3))
	if(int(k/s)==0):
		print(0)
	else:
		while(ans):
			if(a[0]*(ans**3)+a[1]*(ans**2)+a[2]*(ans)+a[3]<=k or ans==0):
				print(ans)
				break
			ans -= 1
