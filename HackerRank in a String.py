from collections import defaultdict

d = defaultdict(int)
a = 'hackerrank'
for i in range(len(a)):
	d[a[i]] += 1
for _ in range(int(input())):
	q = defaultdict(int)
	st = input()
	for i in range(len(st)):
		q[st[i]] += 1
	b = list(set(a))
	c = 'hackerrank'
	for i in range(len(b)):
		if(d[b[i]] <= q[b[i]]):
			flag = 0
			c = c.replace(b[i],'')
			if(len(c) == 0):
				break
		else:
			flag = 1
			break
	if(flag == 0):
		print('YES')
	else:
		print('NO')
