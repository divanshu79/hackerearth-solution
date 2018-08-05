st = input()
a = ['a','e','i','o','u']
b = []
count = 0
for i in range(len(st)):
	if(st[i] in a):
		count += 1
	else:
		b.append(count)
		count = 0
	b.append(count)
print(b)

if(len(b)==0):
	print(0)
else:
	print(max(b))
