for _ in range(int(input())):
     a = int(input())
     b = list(map(int,input().split()))
     c = b[:len(b)//2]
     d = b[len(b)//2:]
     print(sum(c)*sum(d))
          
