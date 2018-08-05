c = '11111111111111111111111111111111'
for _ in range(int(input())):
	n = int(input())
	b = bin(n)[2:]
	k = b.replace('1','2').replace('0','1').replace('2','0')
	s = (k[::-1]+c)[:32]
	print(len(s))
	#s = s[:33]
	s = s[::-1]
	print(int(s,2))
