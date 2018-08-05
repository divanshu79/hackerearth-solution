for i in range(int(input())):
    a,b,c = list(map(int,input().split()))
    if(c==0):
        print(a//b)
    else:
        x = a/b
        k = len(str(int(x)))
        y = pow(10,c)
        z = str(int(x*y))
        if(a>=b):
            z = z[0:k]+'.'+z[k:len(z)]
        else:
            z = '0.'+z
        print(z)
