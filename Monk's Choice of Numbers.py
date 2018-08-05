t = int(input())
for i in range(0,t,1):
    m = list(map(int,input().split()))
    print(m[0])
    n = list(map(int,input().split()))
    g=[]
    for j in n:
        bi = bin(j).count('1')
        print(bi)
        g.append(bi)
        print(g)
    g.sort()
    print(g)
    a = 0
    for i in range(m[0]-m[1],m[0],1):
        a = a+g[i]
    print(a)


    
