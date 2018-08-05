for i in range(0,int(input()),1):
    n = list(map(int,input().split()))
    if(n[1]%2==0):
        ans = n[1]-2
        if(ans>=n[0]):
            print(ans)
        else:
            ans = n[0]&n[1]
            print(ans)
    else:
        ans = n[1]-1
        print(ans)
        
        
