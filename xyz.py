import math

a,b,c,m = list(map(int,input().split()))
x = (b*(math.log(a,c)) - 1)%m
print(x)
d = 0
ans = 1
print(pow(c,x))
while(x>0):
        if(x>=1):
                ans = ans*c
                x = x-1

                
        if(x<1):
                ans = ans+pow(c,x)
                break
        #print(d)
        print(ans)
if(x>0 and x<1):
        d = d+ pow(c,x)
print(ans+d)
#print(d)
