import requests
from bs4 import BeautifulSoup

## Define URL
url = input("What website do you want to scrape? ")

## How many Lines
num_lines = int(input("The number of lines please"))


# response = requests.get(url)

# print(response.status_code)



# htmlText = response.text

# soup = BeautifulSoup(htmlText, 'html.parser')

# paragraphs = soup.find_all('p')

# # print(paragraphs)

# for line in paragraphs[:num_lines]:
#     print(line.text.strip())    

