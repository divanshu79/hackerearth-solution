n = int(input())

for i in range(0,n,1):
    s1 = input()
    s2 = input()
    ses1 = set(s1)
    ses2 = set(s2)
    if(len(ses1) != len(ses2)):
        print('NO')
    else:
        arr1 = list(ses1)
        arr2 = list(ses2)
        count = 0
        for i in range(0,len(ses1),1):
            for j in range(0,len(ses2),1):
                if(arr1[i]==arr2[j]):
                    count = count + 1
                else:
                    count = count
        if(count == len(ses1)):
            print('YES')
        else:
            print('NO')
