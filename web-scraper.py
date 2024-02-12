import requests
from bs4 import BeautifulSoup

# Prompt the user to enter the URL of the website to scrape
url = input("Enter the URL of the website to scrape: ")

# Prompt the user to enter the number of lines they would like to see
num_lines = int(input("How many lines would you like to display? "))

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Here you will need to know the HTML structure to extract the right content.
    # For example, let's say we are looking for 'p' tags for paragraphs
    content = soup.find_all('p')

    # Limit the output to the number of lines the user specified
    for line in content[:num_lines]:
        print(line.text.strip())
else:
    print(f'Failed to retrieve the webpage: {response.status_code}')