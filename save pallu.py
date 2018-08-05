a = int(input())
s = 0
for i in range(0,a-1,1):
	k = 1
	for j in range(a,i,-1):
		k = k*j
		#print("k "+str(k))
	s = s+k
	#print("s "+str(s))
print(s)
