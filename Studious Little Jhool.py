import bisect
d = [0]
for i in range(5,1000,5):
	d.append(12*i)
#print(d)

for _ in range(int(input())):
	n = int(input())
	if(n%2 != 0 or n<10):
		print('-1')

	else:
		s = t= 0
		c = p = 0
		o = n
		while(n>=10):
			if(n%12 == 0):
				s += n//12
				c = 0
				break
			elif(n%12 != 0 and n%10 == 0):
				s += n//10 - bisect.bisect_right(d,n) + 1
				c = 0
				break
			elif(n%12 != 0 and n%10 != 0):
				s += 1
				n -= 12
				c = 1
		#print(o)
		while(o>=10):
			if(o%12 == 0):
				t += o//12
				p = 0
				break
			elif(o%12 != 0 and o%10 == 0):
				t += o//10 - bisect.bisect_right(d,o) + 1
				#print(bisect.bisect_right(d,o))
				c = 0
				break
			elif(o%12 != 0 and o%10 != 0):
				t += 1
				o -= 10
				p = 1
		if(c == 0 and p == 0):
			print(min(s,t))
		elif(c!= 0 and p == 0):
			print(t)
		elif(c == 0 and p!= 0):
			print(s)
		else:
			print('-1')
		#print((c,p))
		#print((s,t))
