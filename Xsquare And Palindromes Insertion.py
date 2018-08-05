for i in range(int(input())):
	st = input()
	d = {}
	for i in range(26):
		d[chr(97+i)] = 0

		
	for j in range(len(st)):
		d[st[j]] += 1

		

	count = 0
	for i in range(26):
		if(d[chr(97+i)]%2!=0):
			count += 1

			
	if(count >0):
		print(count-1)
	else:
		print("0")
