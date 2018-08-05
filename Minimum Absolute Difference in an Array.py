import itertools
n = int(input())
x = list(map(int,input().split()))
z = list(itertools.combinations(x,2))
a = []
for i in range(len(z)):
	a.append(abs(z[i][0]-z[i][1]))
print(min(a))
