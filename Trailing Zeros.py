n = int(input())
p = 5
if(n<p):
	print("0")
else:
	x = 0
	while(n>p):
		x =x + int(n/p)
		if(n>=p*5):
			p = p*5
		else:
			break
	print(int(x))
