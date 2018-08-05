for i in range(int(input())):
        n = int(input())
        sq = n**(1/2.0)
        count = 0
        for i in range(int(sq),0,-1):
                if(n%i!=0):
                        count += 1
                else:
                        break
        #print(int(sq)-count)
        a = int(sq)-count
        b = int(n/a)
        #print(b)
        sum = 0
        while(1):
                if(a>b):
                        a = a-b
                        sum += 1
                elif(b>a):
                        b = b-a
                        sum += 1
                else:
                        sum += 1
                        break
        print(sum)
