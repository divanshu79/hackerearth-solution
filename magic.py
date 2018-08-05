t = int(input())

for i in range(0,t,1):
    n = int(input())
    count = 0
    for i in range(0,n,1):
        if(n%2 == 0):
            n = n/2
            count = count+1
        else:
            n = (n-1)/2
            count = count+2
    print(count)
