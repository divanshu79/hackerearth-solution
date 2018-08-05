import requests
from bs4 import BeautifulSoup
k = "Harry-Potter"
r = requests.get("http://www.ebay.in/sch/Books-Magazines/267/i.html?_from=R40&_nkw=harry%20potter")
soup = BeautifulSoup(r.content, "html.parser")
#print(soup)
flag = 0
list = []
for i in soup.find_all('li'):
    book_title = i.find_all('a',{'class':'vip'})
    #print(book_title)
    for j in book_title:
        #print(j.text)
        list.append(j.text)
##        print(j.get("href"))
        flag += 1
#print(flag)
c = 0
for i in soup.find_all('li'):
    book_img = i.find_all('img',{'class':'img'})
    #print(book_title)
    for j in book_img:
        #print(j.get('src'))
        c += 1
#print(c)
for i in soup.find_all('li'):
    book_prize = i.find_all('span',{'class':'bold'})
    #print(book_prize)
    f_prize = 0
    #print(book_title)
    for j in book_prize:
        if j != 0:
            print(j)
            if f_prize == 0:
                prize = j.text
                c += 1
                f_prize += 1
                #print(prize)
#print(c)
