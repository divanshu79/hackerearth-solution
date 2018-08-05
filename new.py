l = int(raw_input())
n = int(raw_input())
while n:
	n -= 1
	w = int(raw_input())
	h = int(raw_input())
	if l>w or l>h:
	`print` 'UPLOAD ANOTHER'
	elif l==w and l==h:
	print 'ACCEPTED'
	else :
	print 'CROP IT'
