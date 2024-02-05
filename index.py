from bs4 import BeautifulSoup
import requests
import csv

digiato_url = "https://digiato.com/daily-timeline"

page_count = 10
news_title_tags = []
news_description_tags = []


for i in range(page_count):
    url = digiato_url + "/page/" + str(i + 1)
    response = requests.get(url)
    result = BeautifulSoup(response.text, "html.parser")
    news_title_tags += result.find_all(["a"], class_="rowCard__title")
    news_description_tags += result.find_all(
        ["p"], class_="rowCard__description")


if (
    len(news_title_tags) != 0 and
    len(news_description_tags) != 0 and
    len(news_title_tags) == len(news_description_tags)
):
    news_titles = []
    news_links = []
    news_descriptions = []
    for i in range(len(news_title_tags)):
        news_titles.append(news_title_tags[i].text)
        news_links.append(news_title_tags[i]["href"])
        news_descriptions.append(news_description_tags[i].text)

    counters = [i for i in range(1, len(news_titles) + 1)]
    rows = zip(counters, news_titles, news_links, news_descriptions)

    file_path = "latest_news.csv"

    # Write the rows to a CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Counter', 'Title', 'Link', 'Description']
        )  # Write header
        writer.writerows(rows)  # Write rows
    print("All", page_count * 20, "added to latest_news.csv file successfully.")
