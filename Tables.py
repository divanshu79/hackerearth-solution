t = int(input())
a = []*t
dp = [1]*t
for i in range(t):
	n=int(input())
	a.append(n)

for i in range(1,t):
	if a[i]>a[i-1]:
		dp[i] = dp[i-1]+1
	else:
		dp[i]=1

for j in range(t-2,-1,-1):
	if a[j]>a[j+1] and dp[j]<=dp[j+1]:
		dp[j]=dp[j+1]+1
		
print(sum(dp))
