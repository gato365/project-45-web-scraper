import requests
from bs4 import BeautifulSoup

## Define URL
url = input("What website do you want to scrape? ")

## How many Lines
num_lines = int(input("The number of lines please. "))


response = requests.get(url)




if response.status_code == 200: 
    htmlText = response.text

    soup = BeautifulSoup(htmlText, 'html.parser')

    paragraphs = soup.find_all('p')

    for line in paragraphs[:num_lines]:
        print(line.text.strip()) 
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")

