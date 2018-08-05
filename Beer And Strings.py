d = {}
for i in range(26):
	d[chr(97+i)] = 0

n = input()
for i in range(len(n)):
	d[n[i]] += 1


count = 0
for _ in range(int(input())):
	st = input()
	k = {}
	for i in range(len(st)):
		k[st[i]] = 0

	for i in range(len(st)):
		k[st[i]] += 1

	a = []
	flag = 0

	for i in range(len(st)):
		if(st[i] not in d):
			flag = 1
			break
		else:
			if(d[st[i]]>=k[st[i]]):
				flag = 0
			elif(d[st[i]]<k[st[i]]):
				flag = 1
				break

	if(flag == 0):
		count += 1
print(count)
