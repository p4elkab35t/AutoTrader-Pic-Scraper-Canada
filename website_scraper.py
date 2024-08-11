import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
import requests
import re

options = ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')

def get_plain(URL="https://www.google.com"):

# Send a GET request to the URL
    response = requests.get(URL)

# Get the HTML content of the page
    html_content = response.text

# Print the HTML content
    return html_content

def get_images(plainHTML):
    regex = r'"image":\s*\[\s*("https?://[^"]+"\s*(,\s*"https?://[^"]+")*)\s*\]'
    matches = re.search(regex, plainHTML, re.MULTILINE)
    # print(matches)
    if matches:
    # Get the matched group (the part inside the brackets)
        links_string = matches.group(1)
    # Extract individual links by splitting on comma
        links = [link.strip().strip('"') for link in links_string.split(',')]
        # print(links)
        return links
    else:
        # print("No matches found.")
        return []
# def scrape_page(page_link):
#     driver = webdriver.Chrome(options=options)
#     if "https://" not in page_link:
#         page_link = "https://" + page_link
    
#     print(page_link)
#     driver.get(page_link)
#     content = driver.page_source
#     # print(content)
#     return content

# def parse_content(content, location, source, classes):
#     results = []
#     soup = BeautifulSoup(content, 'html.parser')
#     print(soup.find_all(attrs={'class': classes}))
#     #wirte in file
#     with open("temp_links.txt", "w") as file:
#         file.write(str(soup))
#     for a in soup.findAll(attrs={'class': classes}):
#         print(a)
#         name = a.find(location)
#         if name not in results:
#             results.append(name.get(source))
#     print(results)
#     return results

# gallery-thumbnail ng-star-inserted
