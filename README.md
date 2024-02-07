
# Digiato 200 Latest News 

As you can understand this project is a web scraper, that sends multiple GET requests to https://digiato.com/ news website and get its data, and process througth them and extracts news titles and links and their descriptions. 
Finally it saves these list of latest news data in a file which name is *latest_news.csv* in local route.




## Package Dependencies:

 - requests
 - beautifulsoup4


## Deployment

To run this project 

```python
  python3 index.py
```


## Features

- if you want to change number of news you can change the value of *page_count* in the code.
- if you want to change the csv file name or path you can change the *file_path* variable.


## Sample Data Table
<img width="1196" alt="Screenshot 1402-11-18 at 1 21 43 in the afternoon" src="https://github.com/fatemezka/digiato-news-webscaper/assets/77573694/c086668d-f28e-4411-8012-ef03c0d4ee87">
