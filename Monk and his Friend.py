t = int(input())

for i in range(0,t,1):
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        c = c^i
    print(bin(c).count('1'))
    
