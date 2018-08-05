k = 10000003
d, sieve = {0:1}, [True] * (k)
for p in range(2, int(k**(1/2))):
        if sieve[p]:
                for i in range(p * p, k, p):
                        sieve[i] = False

for i in range(1,k,1):
        if sieve[i]:
                d[len(d)] = ((d[len(d)-1]%1000000007)*i)%1000000007
#print(len(d))




for i in range(int(input())):
	n = int(input())
	print(d[n])
