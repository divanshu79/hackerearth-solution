from collections import defaultdict

def apk(p,d,o):
    for i in p:
        if o not in d[i]:
            d[i].append(o)

for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    d = defaultdict(list)
    q = defaultdict(list)
    #d[1] = 1
    flag = 0
    totel = []
    for i in range(b):
        j = input()
        totel.append(j)
    for i in range(len(totel)):
        x = totel[i]
        y = x[::-1]
        f = int(x[0])
        s = int(y[0])
        print(x,y)
        
        if(x[2] == '!'):
            d[f].append(s)
            d[s].append(f)
            k = q[f]
            l = q[s]
            apk(k,d,s)
            apk(l,d,f)
            if s in q[f]:
                flag = 1
                break
        else:
            k = q[f]
            l = q[s]
            q[f].append(s)
            q[s].append(f)
            apk(k,q,s)
            apk(l,q,f)
            d[f].extend(d[s])
            d[f] = list(set(d[f]))
            g = q[f]
            for i in g:
                d[i].extend(d[f])
                d[i] = list(set(d[i]))
            if s in d[f]:
                flag = 1
                break

    if(flag == 1):
        print('NO')
        #break
    else:
        print('YES')

    print(d)
    print(q)








            
