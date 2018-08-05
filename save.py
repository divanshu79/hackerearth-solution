a = list(map(int,input().split()))
s = int(input())
b = [10,50,100,500,1000,5000]
count = 0
for i in range(0,6,1):
	if(a[i]==0):
		count += 1
	else:
		count = count
		break
summ = a[0]*10+a[1]*50+a[2]*100+a[3]*500+a[4]*1000+a[5]*5000
k = int(summ/s)
x = int((summ-b[count])/s)
print(k-x)
st = ''
for i in range(x+1,k+1,1):
        st = st + str(i) +" "
print(st)
