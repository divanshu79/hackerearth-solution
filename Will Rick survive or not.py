for _ in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	count =0
	k = 0
	min = 0
	flag = 0
	for i in range(len(a)):
		if(k>=6):
			min += 1
			if(a[i]>i+min):
				count += 1
				k = 1
			else:
				flag = 1
				break
		else:
			if(a[i]>i+min):
				count += 1
				k += 1
			else:
				flag = 1
				break
	if(flag != 1):
		print("Rick now go and save Carl and Judas")
	else:
		print("Goodbye Rick")
		print(count)
