from bs4 import BeautifulSoup
import requests
import re

digiato_url = "https://digiato.com/daily-timeline"

news_titles = []
news_descriptions = []

for i in range(10):
    url = digiato_url + "/page/" + str(i + 1)
    response = requests.get(url)
    result = BeautifulSoup(response.text, "html.parser")
    news_titles += result.find_all(["a"], class_="rowCard__title")
    news_descriptions += result.find_all(["p"], class_="rowCard__description")

# regex
# some_tags = result.find_all(re.compile("\$.*"), limit=3)


if (
    len(news_titles) != 0 and
    len(news_descriptions) != 0 and
    len(news_titles) == len(news_descriptions)
):
    for i in range(len(news_titles)):
        print(i+1, news_titles[i].text, "")
        print(i+1, news_titles[i]["href"], "")
        print(i+1, news_descriptions[i].text, "")
        print("-------------")
