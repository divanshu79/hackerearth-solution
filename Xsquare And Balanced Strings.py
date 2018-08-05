from collections import Counter


for i in range(int(input())):
	n = input()
	d = Counter(n)
	
	flag = 0
	for i in range(97,123,1):
		if(d[chr(i)] %2 != 0):
			flag = 1
			break

	if(flag == 1):
		print('-1')
	else:
		print('1')
