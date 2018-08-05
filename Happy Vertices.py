from collections import defaultdict

def dfs(d,s):
        st = [s]
        vi[s] = True
        visited_order = []
        while st:
                v = st.pop()
                visited_order.append(v)
                for i in d[v]:
                        if vi[i] == False:
                                st.append(i)
                                vi[i] = True
                                pa[i] = v
                                count[v] += 1

d = defaultdict(list)
a,b = map(int,input().split())
conn_comp = 0
ha = 0
vi = [False]*(a+1)
pa = [0]*(a+1)
count = [0]*(a+1)
for i in range(b):
        x,y = list(map(int,input().split()))
        d[x].append(y)
        d[y].append(x)
	
for i in range(1,a+1):
        if vi[i] == False:
                dfs(d,i)
                conn_comp += 1
for i in range(1,a):
        if count[i] > count[pa[i]]:
                ha += 1
print(ha - (conn_comp//2) -1)
