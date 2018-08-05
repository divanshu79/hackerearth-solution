def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)


for i in range(int(input())):
    n,x = list(map(int,input().split()))
    if(n>=1000003):
        print('0')
    else:
        s = treefactorial(n)%1000003
        print(s*x)