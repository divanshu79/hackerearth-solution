for i in range(int(input())):
	nums = list(map(int, input().split()))
	N, M = nums[0], nums[1]
	binM = str(bin(M)[2:])[::-1]
	index, s = 0, ""
	for j in binM:
		if j == "1": s = "(" + str(N) + "<<" + str(index) + ")" + " + " + s
		index += 1
	print(s[0:len(s) - 2])
