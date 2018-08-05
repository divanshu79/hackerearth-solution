str1=input()
n=int(input())
count=0
s=set(list(str1))
for i in range(n):
    str2=input()
    str2=set(list(str2))
    if str2.issubset(s):
    	    count+=1
print(count)	
