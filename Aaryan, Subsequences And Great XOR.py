t = int(input())
c = 0
arr = input().split()
n = [0]*t
for i in range(0,t,1):
    n = int(arr[i])
    c = c|n
print (c)

