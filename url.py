


p = []
for link in soup.find_all("a"):
	a = link.get("href")
	if(a != None):
		if j in a and "dp" in a and "#customerReviews" not in a:
			print(a)
