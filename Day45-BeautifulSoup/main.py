from bs4 import BeautifulSoup

with open(file="website.html", encoding="utf8") as myfile:
   contents = myfile.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.a)

all_anchor = soup.findAll('a')
print(all_anchor)

for tags in all_anchor:
   print(tags.getText())

for links in all_anchor:
   print(links.get("href"))