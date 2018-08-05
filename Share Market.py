import itertools

for _ in range(int(input())):
	n = int(input())
	cost = list(map(int,input().split()))
	cost.sort()
	d = {}
	for i in range(1,n+1):
		d[i] = list(itertools.combinations(cost,i))

	share = int(input())
	lst = list(map(int,input().split()))
	cost_share = list(map(int,input().split()))

	for i in range(share):
		p = d[lst[i]]
		for j in range(len(p)):
			c = sum(p[j])
			if(c == cost_share[i]):
				flag = 1
				break
			elif(c > cost_share[i]):
				flag = 0
				break
			else:
				flag = 0

		if(flag == 1):
			print("Yes")
		else:
			print("No")
