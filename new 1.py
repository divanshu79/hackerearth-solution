'''
# Read input from stdin and provide input before running code
 
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
# print 'Hello World!'
l = int(raw_input())
n = int(raw_input())
while n:
	n -= 1
	sizes = raw_input().split(' ')
	w, h = int(sizes[0]), int(sizes[1])
	if w< l or h < l:
		print 'UPLOAD ANOTHER'
	elif w == h  and w >=l:
		print 'ACCEPTED'
	else:
		print 'CROP IT'
