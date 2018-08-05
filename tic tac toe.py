for _ in range(int(input())):
	n = int(input())
	k = n-1
	m = 1000000007
	ans = (((k*(k+1))*(2*k+1))//6)%m
	#ans = ans//6

	#print(ans)

	x = (n-1)//2
	anss = int((x**2)*n)%1000000007

	#print(anss)


	print(str(anss)+" "+str(ans))
