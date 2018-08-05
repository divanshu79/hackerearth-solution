n = int(input())
arr = list(map(int,input().split()))
distinctElement = len(set(arr))
arrMap = dict()
for i in set(arr):
    arrMap[i]=0

print(arrMap)
