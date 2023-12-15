from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import time

# List of Dota 2 version elements
patches = [
    "Version 7.08", "Version 7.09", "Version 7.10", "Version 7.11", "Version 7.12",
    "Version 7.13", "Version 7.13b", "Version 7.14", "Version 7.15", "Version 7.16",
    "Version 7.17", "Version 7.18", "Version 7.19", "Version 7.19b", "Version 7.19c",
    "Version 7.19d", "Version 7.20", "Version 7.20b", "Version 7.20c", "Version 7.20d",
    "Version 7.20e", "Version 7.21", "Version 7.21b", "Version 7.21c", "Version 7.21d",
    "Version 7.22", "Version 7.22b", "Version 7.22c", "Version 7.22d", "Version 7.22e",
    "Version 7.22f", "Version 7.22g", "Version 7.22h", "Version 7.23", "Version 7.23a",
    "Version 7.23b", "Version 7.23c", "Version 7.23d", "Version 7.23e", "Version 7.23f",
    "Version 7.24", "Version 7.24b", "Version 7.25", "Version 7.25a", "Version 7.25b",
    "Version 7.25c", "Version 7.26", "Version 7.26a", "Version 7.26b", "Version 7.26c",
    "Version 7.27", "Version 7.27a", "Version 7.27b", "Version 7.27c", "Version 7.27d",
    "Version 7.28", "Version 7.28a", "Version 7.28b", "Version 7.28c", "Version 7.29",
    "Version 7.29b", "Version 7.29c", "Version 7.29d", "Version 7.30", "Version 7.30b",
    "Version 7.30c", "Version 7.30d", "Version 7.30e", "Version 7.31", "Version 7.31b",
    "Version 7.31c", "Version 7.31d", "Version 7.32", "Version 7.32b", "Version 7.32c",
    "Version 7.32d", "Version 7.32e", "Version 7.33", "Version 7.33b", "Version 7.33c",
    "Version 7.33d", "Version 7.33e", "Version 7.34", "Version 7.34b", "Version 7.34c",
    "Version 7.34d", "Version 7.34e"
]

dota2_wiki_urls = ["https://dota2.fandom.com/wiki/" + patch.replace(" ", "_") for patch in patches]
# print(dota2_wiki_urls)

dota2_website_urls = ["https://www.dota2.com/patches/" + patch.split(" ")[1] for patch in patches]
# print(dota2_website_urls)


wiki_folder_name = "WikiNotesRaw"
original_folder_name = "OriginalNotesRaw"

for folder in [wiki_folder_name, original_folder_name]:
    if not os.path.exists(folder):
        os.makedirs(folder)


def download_html(url, folder_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = url.split('/')[-1] + '.html'

        with open(os.path.join(folder_name, filename), 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Downloaded and saved {filename} in {folder_name}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")


def download_html_with_selenium(urls, folder_name):
    driver = webdriver.Chrome()
    for url in urls:
        try:
            driver.get(url)
            time.sleep(30)
            html_content = driver.page_source
            filename = url.split('/')[-1] + '.html'

            with open(os.path.join(folder_name, filename), 'w', encoding='utf-8') as file:
                file.write(html_content)
            print(f"Saved HTML for {url}")

        except Exception as e:
            print(f"An error occurred while processing {url}: {e}")

    # Close the WebDriver
    driver.quit()

    print("All pages have been processed.")


# Download the HTML content for each URL in set 1
# for url in dota2_wiki_urls:
#     download_html(url, wiki_folder_name)
# print("Completed downloading patch notes from Dota 2 Wiki."

# Download the HTML content for each URL in set 2
download_html_with_selenium(dota2_website_urls, original_folder_name)
print("Completed downloading patch notes from the official Dota 2 Website.")