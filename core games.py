a,b = list(map(int,input().split()))
arr = []
for i in range(a):
	arr.append(i+1)
k = 0
st = ''


while(len(arr)!=2):
	if(len(arr)!=2):
		k = b-1
		p = (k%(len(arr)))
		st = st+str(arr[p])+" "
		arr = arr[p+1:len(arr)]+arr[:p]
		print(st)
		print(arr)
	else:
		break
if(b%2!=0):
	print(st+str(arr[0])+" "+str(arr[1]))
else:
	print(st+str(arr[1])+" "+str(arr[0]))
