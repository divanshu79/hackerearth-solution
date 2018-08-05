a,b = list(map(int,input().split()))
arr = []
for i in range(a):
	arr.append(i+1)
#print(arr)
k = 0
sum = 0
st = ''


while(len(arr)!=1):
	if(k == 0):
		st += str(arr[b-1])+" "
		s = b-1
		arr = arr[:b-1]+arr[b:len(arr)]
		print(s)
		k = k+b
		print('x '+st)
		print(arr)
	k = b
	if(k==b):
		k = k+s
		p = (k%(a-1))-1
		print("value of p "+str(p))
		if(len(arr)!=0):
			st += str(arr[p])+" "
			arr = arr[:p]+arr[p+1:len(arr)]
			s = len(arr[:p])
			print("value of s "+str(s))
		else:
			break
		print(arr)
		print('y '+st)
print(st+str(arr[0]))
