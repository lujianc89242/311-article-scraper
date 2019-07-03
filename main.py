import requests
from bs4 import BeautifulSoup
outFile = open("output.txt","w")
r = requests.get("https://portal.311.nyc.gov/all-articles/")
c = r.content

#print(c)

soup = BeautifulSoup(c, "html.parser")

#print(soup.prettify())  # parser the source code and format the html with indentations

ul = soup.find_all("ul",{"class":"all-az-kas"})
li = ul[0].find_all("li")

article_ctr = 0
for item in li:
    a = item.find_all("a")
    for item in a:
        #print(item.text)
        output = item.text.strip() + "\n"
        outFile.write(output)
        article_ctr = article_ctr + 1
        
print("total: ", article_ctr)

outFile.close()
