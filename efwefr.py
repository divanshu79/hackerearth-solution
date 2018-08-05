n = int(input())

for i in range(0,n,1):
    s1 = input()
    s2 = input()
    arr1 = list(s1)
    arr2 = list(s2)
    for i in range(0,len(s1),1):
            for j in range(0,len(s2),1):
                if(arr1[i]==arr2[j]):
                    l=s1
                    break
                else:
                    l=s2
    if(l==s1):
        print ('Yes')
    else:
        print('No')
        
            
