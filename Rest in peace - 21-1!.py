n = int(input())
for i in range(n):
	s = input()
	flag = 0
	if(int(s)%21!=0):
		if('21' in s):
			flag = 1
		else:
			flag = 0
	else:
		flag = 1


	if(flag == 0):
		print("The streak lives still in our heart!")
	else:
		print("The streak is broken!")
