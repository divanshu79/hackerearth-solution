for _ in range(int(input())):
	st = input()
	d = {}
	for i in range(25):
		d[chr(97+i)+"-"+chr(98+i)] = 1
		d[chr(98+i)+"-"+chr(97+i)] = 1
	d['a'+'-'+'z'] = 1
	d['z-a'] = 1


	flag = 0
	for i in range(len(st)-1):
		if(st[i]+'-'+st[i+1] not in d):
			flag = 1
			break
		else:
			flag = 0

		#print(st[i]+'-'+st[i+1])

	if(flag == 1):
		print("NO")

	else:
		print("YES")

