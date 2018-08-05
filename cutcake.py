ts = int(raw_input())
while ts:
    num=int(raw_input())
    if num==1:
        print 0
    elif num==2:
        print 1
    else :
        sum =0
        i=1
        while 1:
            sum=sum+i
            if sum >= num-1:
                break
            i=i+1
        ts = ts-1
        print i
        
