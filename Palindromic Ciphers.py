d = {}
for i in range(26):
	d[chr(97+i)] = i+1


for _ in range(int(input())):
	st = input()
	if(len(st)%2==0):
		x = len(st)//2
		a = st[:x]
		b = st[x:len(st)]
		b = b[::-1]
		if(a==b):
			print("Palindrome")
		else:
			k = 1
			for i in range(len(st)):
				k = k*d[st[i]]
			print(k)
	else:
		x = len(st)//2
		a = st[:x]
		print(a)
		b = st[x+1:len(st)]
		print(b)
		b = b[::-1]
		if(a==b):
			print("Palindrome")
		else:
			k = 1
			for i in range(len(st)):
				k = k*d[st[i]]
			print(k)
			
