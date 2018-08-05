t = int(input())
for i in range(0,t,1):
    arr = list(map(int,input().split()))
    a = list(bin(arr[1])[2:])[::1]
    s = ""
    for i in range(len(a)-1,-1,-1):
        if(a[i]=="1"):
            s = "(" + str(arr[0]) + "<<" + str(len(a)-i-1) + ")" + "" + ""+ " + " + s
    print(s[0:len(s) - 2])
