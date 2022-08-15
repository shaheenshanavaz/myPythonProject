from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/")
ycwebsite = response.text

soup = BeautifulSoup(ycwebsite,"html.parser")

article_tag =soup.findAll('a',class_= 'titlelink')
print(article_tag)
article_text = []
article_link = []
for article in article_tag:
    text = article.getText()
    article_text = article_text.append(text)
    article_link = article_link.append(article.get('href'))
article_upvote = soup.findAll(name = 'span',class_ = "score").getText()
print(f"Article Text: {article_text}")
print(f"Article Link: {article_link}")
print(article_upvote)
print(int(article_upvote.split()[0]))