import itertools 
t = int(input())
for i in range(0,t,1):
    n = int(input())
    value = list(map(int,input().split()))
    s = int(input())
    flag = 0
    if(s == 0):
        print('YES')
    else:
        for i in range(1,n+1):
            for j in itertools.combinations(value , i):
                
                if(sum(j) == s):
                    flag = 1
                    break
            if(flag == 1):
                break
        if(flag == 1):
            print('YES')
        else:
            print('NO')
