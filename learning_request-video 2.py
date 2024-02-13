import requests
from bs4 import BeautifulSoup

## Define URL
url = "https://en.wikipedia.org/wiki/Taylor_Swift"

## How many Lines
num_lines = 4


response = requests.get(url)

print(response.status_code)

print(response.text)