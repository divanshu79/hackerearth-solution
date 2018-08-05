import requests
from bs4 import BeautifulSoup
k = "Harry-Potter"
j = "http://www.amazon.in/"
r = requests.get("https://www.snapdeal.com/search?keyword=harry%20potter&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy")
soup = BeautifulSoup(r.content, "html.parser")

g = soup.find_all('div',{'class':'product-tuple-image '})

for i in g:
    book_img = i.find_all('source',{'class':'product-image'})
    #print(book_img)
    #for j in book_img:
        #print(j.get('srcset'),j.get('title'))
c = 0
for i in g:
    book_link = i.find_all('a')
    for j in book_link:
        #print(j.get('href'))
        c += 1
#print(c)

for i in soup.find_all('div',{'class':'product-price-row clearfix'}):
    book_link = i.find_all('span',{'class':'lfloat product-price'})
    #print(book_link)
    for j in book_link:
        print(j.get('display-price'))
