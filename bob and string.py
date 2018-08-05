for i in range(int(input())):
	a = input()
	b = input()
	hashA = {}
	hashB = {}
	for i in range(0,26,1):
		hashA[chr(97+i)]=0
		hashB[chr(97+i)]=0
	for i in range(0,len(a),1):
		hashA[a[i]] += 1
	for i in range(0,len(b),1):
		hashB[b[i]] += 1

	count = 0

	for i in range(0,26,1):
		if(hashA[chr(97+i)]-hashB[chr(97+i)]>0):
			count += hashA[chr(97+i)]-hashB[chr(97+i)]
		else:
			count += hashB[chr(97+i)]-hashA[chr(97+i)]

	print(count)
