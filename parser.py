import os
from bs4 import BeautifulSoup

# relative to the project root
directory_path = "OriginalNotesRaw"


def parse_hero_div(div):
    title = div.find('a')
    hero_name = title.find('div').find_next_sibling('div').text
    print(hero_name)


for filename in os.listdir(directory_path):
    # safeguard to only parse .html files
    if filename.endswith(".html"):
        file_path = os.path.join(directory_path, filename)

        with open(file_path, 'r') as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            # skip directly to the Hero Updates inside the patch html, ignoring other updates
            hero_changes_div = soup.find('div', string='Hero Updates')
            # all the hero updates are included in the sibling to the div containg 'Hero Updates'
            nested_hero_changes_div = hero_changes_div.find_next_sibling('div')
            nested_hero_changes_div_content = str(nested_hero_changes_div)
            # each hero will have its own set of updates inside of this div
            # so we parse each nested hero div separately
            for hero_div in nested_hero_changes_div.find_all('div', recursive=False):
                parse_hero_div(hero_div)


