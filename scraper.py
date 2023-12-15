import requests
from bs4 import BeautifulSoup

# URL of the Dota 2 patch notes
url = 'https://dota2.fandom.com/wiki/Version_7.34e'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)
heroes_changes = soup.find_all('div', class_='hero-change')
# Iterate over each hero change section and extract relevant information
for change in heroes_changes:
    hero_name = change.find('h2').text  # or appropriate tag and method to extract hero name
    change_details = change.find_all('li')  # Assuming each change is in a list item

    print(f'Hero: {hero_name}')
    for detail in change_details:
        print(f' - {detail.text}')

# Add additional logic as needed to refine data extraction and categorization
