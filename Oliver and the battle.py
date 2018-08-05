from collections import defaultdict
for _ in range(int(input())):
	a,b = list(map(int,input().split()))
	en = []
	for i in range(a):
		x = list(map(int,input().split()))
		en.append(x)
	ans = []
	for c in range(a):
		for p in range(b):
			t = 0
			cl = defaultdict(int)
			op = []
			if(en[c][p] == 1 and cl[en[c][p]] == 0):
				op.append([en[c][p]])
				cl[en[c][p]] = 1
				t += 1
				
				while(op != 0):
					q = op.pop(0)
					if(c+1 <= a and en[c+1][p]==1 and cl[en[c+1][p]] == 0):
						op.append(en[c+1][p])
						cl[en[c+1][p]] = 1
						t += 1
					if(p+1 <= b and en[c][p+1]==1 and cl[en[c][p+1]] == 0):
						op.append(en[c][p+1])
						cl[en[c][p+1]] = 1
						t += 1
					if(c+1 <= a and p+1<=b and en[c+1][p+1]==1 and cl[en[c+1][p+1]] == 0):
						op.append(en[c+1][p+1])
						cl[en[c+1][p+1]] = 1
						t += 1
					if(c+1 <= a and p-1>=0 and en[c+1][p-1]==1 and cl[en[c+1][p-1]] == 0):
						op.append(en[c+1][p-1])
						cl[en[c+1][p-1]] = 1
						t += 1
					if(p-1>=0 and c-1>=0 and en[c-1][p-1]==1 and cl[en[c-1][p-1]] == 0):
						op.append(en[c-1][p-1])
						cl[en[c-1][p-1]] = 1
						t += 1
			ans.append(t)

	print(ans)
					







					
