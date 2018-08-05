for j in range(int(input())):
	st1 = input()
	st1 = list(set(st1))
	st2 = input()
	st2 = list(set(st2))
	
	d = {}

	for i in range(26):
		d[chr(97+i)] = 1

	for i in range(len(st1)):
		d[st1[i]] += 1

	for i in range(len(st2)):
		d[st2[i]] += 1

	flag = 0


	for i in range(26):
		if(d[chr(97+i)] > 2):
			flag = 1
			break
		else:
			flag = 0

	if(flag == 1):
		print("YES")
	else:
		print("NO")
