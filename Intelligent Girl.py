s = input()
c = 0
for i in range(len(s)):
	if(int(s[i]) % 2 == 0):
		c += 1

if(int(s[0])%2 == 0):
	z = 1
else:
	z = 0

st = str(c) + ' '
for i in range(1,len(s)):
	if(int(s[i])%2 == 0):
		st += str(c-z)+' '
		z += 1
	else:
		st += str(c-z)+' '
print(st)
