a,b,c = list(map(int,input().split()))
n = int(input())
x = []
y = []
m = 1000000007
x.append((a*c)%m)
y.append((b*c)%m)
for i in range(1,n,1):
	x[i] = (((((x[i-1]*a)%m)*b)%m)*c)%m + (((x[i-1]*a)%m)*b)%m + (((x[i-1]*a)%m)*c)%m
	x[i] = x[i]%m
	y[i] = (((((y[i-1]*b)%m)*c)%m)*a)%m + (((y[i-1]*b)%m)*a)%m + (((y[i-1]*b)%m)*c)%m
	y[i] = y[i]%m

first_min_x = x[0]
second_min_x = x[1]
first_min_y = y[0]
second_min_y = y[1]
count = 0
flag = 0
s = []
p = []

for i in range(1,n,1):
	if(x[i]<first_min_x):
		second_min_x = first_min_x
		first_min_x = x[i]
		count += 1
		s.append(count)
	elif(x[i]>first_min_x and x[i]>second_min_x):
		count += 1
	elif(x[i]>first_min_x and x[i]<second_min_x):
		second_min_x = x[i]
		count += 1
		
	elif(y[i]<first_min_y):
		second_min_y = first_min_y
		first_min_y = y[i]
		flaf += 1
		p.append(flag)
	elif(y[i]>first_min_y and y[i]>second_min_y):
		count += 1
	elif(y[i]>first_min_y and y[i]<second_min_y):
		second_min_y = y[i]
		flag += 1

if(s[len(s)-1]==p(len(p)-1)):
	if(first_min_x>=first_min_y):
		print(first_min_y+second_min_x)
	else:
		print(first_min_x+second_min_y)
else:
	print(first_min_x+first_min_y)
