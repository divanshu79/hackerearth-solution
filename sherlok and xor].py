t = int(input())
for i in range(0,t,1):
    tn = int(input())
    count = 0
    flag = 0
    n = list(map(int,input().split()))
    for i in range(0,len(n),1):
        if(n[i]%2 == 0):
            count = count+1
        else:
            flag = flag +1
    print(count*flag)
            
