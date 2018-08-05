for _ in range(int(input())):
	n,m = list(map(int,input().split()))
	x = list(map(int,input().split()))
	in_class = set(x[:n])
	outof_class = x[n:]
	for i in range(m):
		if(outof_class[i] in in_class):
			print('YES')
		else:
			print('NO')
			in_class.add(outof_class[i])
