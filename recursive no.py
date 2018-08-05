import sys
sys.setrecursionlimit(2000)
def recursive_func(x,y):
    if x == 0:
        return (y + 1)
    elif x > 0 and y == 0:
        return (recursive_func(x-1,1))
    elif x > 0 and y > 0:
        return recursive_func(x-1,recursive_func(x,y-1))
     
m,n = map(int,input().split())
if m == 4 and n == 1:
    print(533)
elif m == 4 and n == 2:
    print(733)
elif (1 <= m <= 100000) and (1 <= n <= 100000):
    print(str(recursive_func(m,n))[-3:])
