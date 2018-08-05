for i in range(int(input())):
	a,b,c,k = list(map(int,input().split()))
	s = c-k
	x = b*b
	y = 4*a*s
	u = (x-y)**(1/2)
	root1 = (u-b)/(2*a)
	#print('real '+str(root1))
	root2 = -((u+b)/(2*a))
	#print('real1 '+str(root2))



	if((x-y)<0):
		#print("ans of"+str(a)+" "+str(b)+" "+str(s)+" is   " + "0")
		print("0")


	elif((x-y)>=0):
		if(int(root1) == root1):
			root1 = int(root1)
			#print('r '+str(root1))
		elif(int(root1) != root1 and root1>=0):
			root1 = int(root1) + 1
			#print('r '+str(root1))

		if(root2 == int(root2)):
			root2 = int(root2)
			#print('rs '+str(root2))
		elif(int(root2) != root2 and root2>=0):
			root2 = int(root2) + 1
			#print('rs '+str(root2))

			


		if(root1<0 and root2>=0):
			print(root2)
		elif(root2<0 and root1>=0):
			print(root1)
		elif(root1<0 and root2<0):
			print("0")
		elif(root1>=0 and root2>=0 and root1>root2):
			print(root2)
		elif(root1>=0 and root2>=0 and root1<root2):
			print(root1)

		
