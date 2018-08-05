s = list(input())
sum = 0

for i in range(0,len(s),1):
    sum = sum + int(ord(s[i])-96)
print (sum)
