m = 1000000007
a,b,c = list(map(int,input().split()))
n = int(input())
d = (a*b)%m
e = (a*c)%m
f = (b*a)%m
g = (b*c)%m
h = (a*b*c)%m
#x = (((e%m)*h)%m + ((e%m)*d)%m + ((e%m)*e)%m)%m
#y = (((g%m)*h)%m + ((g%m)*g)%m + ((g%m)*f)%m)%m
x = (e*h + e*m + e*e)%m
y = (g*h + g*g + g*f)%m

k = (e+y)%m
l = (g+x)%m

if(k>l):
	print(l)
else:
	print(k)
print(e,y,g,x)
