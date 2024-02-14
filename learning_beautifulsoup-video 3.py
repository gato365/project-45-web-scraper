import requests
from bs4 import BeautifulSoup

## Define URL
url = "https://en.wikipedia.org/wiki/Taylor_Swift"

## How many Lines
num_lines = 4


response = requests.get(url)

# print(response.status_code)

htmlText = response.text

soup = BeautifulSoup(htmlText, 'html.parser')

paragraphs = soup.find_all('p')

# print(paragraphs)

for line in paragraphs[:num_lines]:
    print(line.text.strip())    

