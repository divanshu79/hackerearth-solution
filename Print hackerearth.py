n = int(input())
st = input()
d1 = {}

p = 'hackerearth'
q = list(set(p))
d2 = {}
for i in q:
	d2[i] = 0
	d1[i] = 0

u = list(set(st))
for i in u:
	d2[i] = 0

for i in p:
	d1[i] += 1

#print(d1)

for i in st:
	d2[i] += 1

#print(d2)

a = []
for i in q:
	x = int(d2[i]/d1[i])
	a.append(x)

print(min(a))
