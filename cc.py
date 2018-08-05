for i in range(int(input())):
	s1 = input()
	s2 = input()
	count = 0
	for j in range(0,len(s1),1):
		flag = 0
		for i in range(0,len(s2),1):
			if(s1[j]==s2[i]):
				flag = 1
				#c = s2.replace(i,"")
				#s2 = c
				b = s2[0:i]
				c = s2[i:len(s2)]
				s2 = b+c
				break

		if(flag == 1):
			count = count+1
		print(s2)
			

	print(2*(len(s1)-count))
	#print(s2)
