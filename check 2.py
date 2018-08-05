a,b = list(map(int,input().split()))
x =[]
for i in range(0,a,1):
        string = input()
        count = 0
        for h in range(0,b,1):
                st = input()
                k = st + string
                k = set(k)
                if(k==26):
                        count +=1
print(count)
