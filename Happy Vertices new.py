from collections import defaultdict

def dfs(d,start):
        stack = [start]
        visited[start] = True
        while stack:
                p = stack.pop()
                for i in d[p]:
                        if visited[i] == False:
                                stack.append(i)
                                visited[i] = True
                                parant[i] = p
                                count[p] += 1
                                

d = defaultdict(list)
visited = defaultdict(bool)
count = defaultdict(int)
parant = defaultdict(int)
m,n = map(int,input().split())
connected_comp = 0
ans = 0
for i in range(n):
        x,y = map(int,input().split())
        d[x].append(y)
        d[y].append(x)

for i in range(1,m+1):
        if visited[i] == False:
                dfs(d,i)
                connected_comp += 1
for i in range(1,m):
        if count[i] > count[parant[i]]:
                ans += 1
print(ans - (connected_comp//2) - 1)
