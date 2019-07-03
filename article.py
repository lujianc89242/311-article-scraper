import requests
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Inches

r = requests.get("https://portal.311.nyc.gov/all-articles/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())  # parser the source code and format the html with indentations

############## Collect All URLs for All Articles ###############
# outFile = open("output.txt","w")
# ul = soup.find_all("ul",{"class":"all-az-kas"})
# li = ul[0].find_all("li")
# url_ctr = 0
# url_list = []
# for item in li:
#     a = item.find_all("a", href=True)
#     for item in a:
#         #print(item.text)
#         href_tag = item['href']
#         article_id = href_tag[21:]
#         output = article_id + "\n"
#         #outFile.write(output)
#         url_ctr = url_ctr + 1
#         full_url = "https://portal.311.nyc.gov/article/?kanumber=" + article_id
#         url_list.append(full_url)
# for url in url_list:
#     print(url)
# outFile.close()

############## Scraping Information From One Page ###############
url = "https://portal.311.nyc.gov/article/?kanumber=KA-02802"
article_req = requests.get(url)
article_content = article_req.content

article_soup = BeautifulSoup(article_content, "html.parser")
article_title = article_soup.find_all("h1", {"class":"entry-title page-title"})
file_name = "./Articles/" + article_title[0].text + ".doc"
file_name_docx = "./Articles(docx)/" + article_title[0].text + ".docx"
ka_content = article_soup.find_all("div", {"class":"ka-content"})[0]
first_card = ka_content.find_all("div",{"class":"card-body"})
outFile = open(file_name,"w")
#outFile.write(first_card[0])

document = Document()
document.add_heading(article_title[0].text,0)

print(ka_content.get_text())

# loop through all descendants recursively for first card
# Nicer formating but may lose Information
# for child in ka_content.descendants:
#     # only capture non-empty NavigableString
#     # print(child, "         ------------          ", child.name)
#     if (str(type(child)) == "<class 'bs4.element.NavigableString'>" and str(child.name) != "style"):
#         print(child.string, "   --------  ", type(child.string), "  ----- ", child.name)
#         output = child.string + '\n'
#         outFile.write(output)
    # if(str(child.name) == "a"):
    #     url_p = child.text + "(" + child['href'] + ")"
    #     print(url_p)
    #     document.add_paragraph(url_p)
    # elif(str(child.name) == "button"):
    #     print(child.text.strip())
    #     document.add_heading(child.text.strip(), level=1)
    # elif(str(child.name) == "strong"):
    #     print(child.text.strip())
    #     document.add_heading(child.text.strip(), level=3)
    # elif(str(child.name) == "li"):
    #     print(child.text.strip())
    #     document.add_paragraph(child.text.strip(), style='List Bullet')
    # elif(str(child.name) == "b"):
    #     print(child.text.strip())
    #     p = document.add_paragraph(child.text.strip())
    #     p.bold = True
    # elif(str(child.name) == "p" and child.contents != []):
    #
    #     if(str(child.contents[0].name) == "strong" and (len(child.contents)==1)):
    #         print("do nothing")
    #     if(str(child.contents[0].name) == "em"):
    #         print("do nothing")
    #     elif(str(child.contents[0].name) == "a"):
    #         print("do nothing")
    #     elif(str(child.contents[0].name) == "span"):
    #         print("do nothing")
        # else:
        # print(child.text.strip())
        # document.add_paragraph(child.text.strip())




# for child in ka_content.descendants:
#     # only capture non-empty NavigableString
#     # print(child, "         ------------          ", child.name)
#     if(str(child.name) == "a"):
#         url_p = child.text + "(" + child['href'] + ")"
#         print(url_p)
#         document.add_paragraph(url_p)
#     if(str(child.name) == "button"):
#         print(child.text.strip())
#         document.add_heading(child.text.strip(), level=1)
#     if(str(child.name) == "li"):
#         print(child.text.strip())
#         document.add_paragraph(child.text.strip(), style='List Bullet')
#     if(str(child.name) == "p" and child.contents != []):
#         if(str(child.contents[0].name) == "a"):
#             print("do nothing")
#         elif(str(child.contents[0].name) == "span"):
#             print("do nothing")
#         else:
#             print(child.text.strip())
#             document.add_paragraph(child.text.strip())



document.save(file_name_docx)
outFile.close()
